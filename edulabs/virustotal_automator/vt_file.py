from vt_base import *
import vt_exeptions
import mimetypes
import requests
import hashlib
import time
import os


class VTFile(VTAutomator):

    def __init__(self, vt_key: str, file: 'os.path'):
        super().__init__()

        if not os.path.exists(file):
            raise vt_exeptions.FileError()
        self.__file: 'os.path' = file

        if not isinstance(vt_key, str) or not vt_key:
            raise vt_exeptions.ApiKeyError()
        self.__vt_key: str = vt_key


    @property
    def file(self) -> 'os.path':
        return self.__file


    @property
    def vt_key(self):
        return self.__vt_key



    def _get_req_file(self):
        if self.requests_amount_limit_counter < 500 and \
                self.requests_per_minute_limit_counter < 4:

            self.set_amount_limit_counter()
            self.set_per_minute_limit_counter()

            headers = {
                "accept": "application/json",
                "x-apikey": self.vt_key
            }
            with open(self.file, 'rb') as file:
                file_hash = file.read()

            hashed = hashlib.sha256(file_hash)
            hex_hash = hashed.hexdigest()

            req: 'requests' = requests.get(self.get_vt_api_file + hex_hash, headers=headers)

            if req.status_code >= 400:
                raise vt_exeptions.RequestFailed()
            if bool(req.json()):
                return req.json()
            else:
                raise vt_exeptions.EmptyContentError()



    def _post_req_file(self, password: str = None):
        if self.requests_amount_limit_counter < 500 and \
                self.requests_per_minute_limit_counter < 4:

            self.set_amount_limit_counter()
            self.set_per_minute_limit_counter()

            mime_type, encoding = mimetypes.guess_type(self.file)

            fh = open(self.file, "rb")
            files = {"file": (str(self.file), fh, mime_type)}

            payload = {"password": password}
            headers = {
                "accept": "application/json",
                "x-apikey": self.vt_key
            }

            if (os.path.getsize(self.file) / 1048576) >= 24:
                api = r'https://www.virustotal.com/api/v3/files/upload_url'
            else:
                api = self.post_vt_api_file

            if password is None:
                req = requests.post(api, files=files, headers=headers)
            else:
                req = requests.post(api, data=payload, files=files, headers=headers)

            fh.close()

            if req.status_code >= 400:
                raise vt_exeptions.RequestFailed()
            if bool(req.json()):
                return req.json()
            else:
                raise vt_exeptions.EmptyContentError()


    def get_file(self):
        rep: int = self._get_req_file().get('data').get('attributes').get('reputation')
        if rep is not None:
            return rep
        else:
            raise FileNotFoundError()


    def post_file(self, password: str = None):
        rep: str = self._post_req_file(password).get('data').get('type')
        if rep is not None:
            return rep
        else:
            raise FileNotFoundError()


    def post_get_file(self, password: str = None):
        self.post_file(password)
        for _ in range(10):
            print('Checking...')
            res_code = self._get_req_file().get('data')
            if len(res_code) > 0:
                return self.get_file()
            else:
                time.sleep(30)
        raise vt_exeptions.EmptyContentError()




    def _get_req_url(self):
        pass

    def _post_req_url(self):
        pass

