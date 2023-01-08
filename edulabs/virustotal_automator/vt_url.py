from vt_base import *
import vt_exeptions
import requests
import base64
import time


class VTUrl(VTAutomator):

    def __init__(self, url: str, vt_key: str):
        super().__init__()

        if not isinstance(url, str):
            raise vt_exeptions.UrlError()
        self.__url: str = url

        if not isinstance(vt_key, str) or not vt_key:
            raise vt_exeptions.ApiKeyError()
        self.__vt_key: str = vt_key

    @property
    def url(self) -> str:
        return self.__url

    @property
    def vt_key(self):
        return self.__vt_key

    def _get_req_url(self) -> dict:
        if self.requests_amount_limit_counter < 500 and \
                self.requests_per_minute_limit_counter < 4:

            self.set_amount_limit_counter()
            self.set_per_minute_limit_counter()

            headers: dict = {
                "accept": "application/json",
                "x-apikey": self.vt_key
            }
            url_id: str = base64.urlsafe_b64encode(f'{self.url}'.encode()).decode().strip('=')
            req: 'requests' = requests.get(url=self.get_vt_api_url + url_id, headers=headers)

            if req.status_code >= 400:
                raise vt_exeptions.RequestFailed()
            elif bool(req.json()):
                return req.json()
            else:
                raise vt_exeptions.EmptyContentError()

    def _post_req_url(self) -> dict:
        if self.requests_amount_limit_counter < 500 and \
                self.requests_per_minute_limit_counter < 4:

            self.set_amount_limit_counter()
            self.set_per_minute_limit_counter()

            payload: str = f"url={self.url}"

            headers: dict = {
                "accept": "application/json",
                "x-apikey": self.vt_key,
                "content-type": "application/x-www-form-urlencoded"
            }
            req: 'requests' = requests.post(self.post_vt_api_url, data=payload, headers=headers)

            if req.status_code >= 400:
                raise vt_exeptions.RequestFailed()
            if bool(req.json()):
                return req.json()
            else:
                raise vt_exeptions.EmptyContentError()

    def get_url(self) -> int:
        rep: int = self._get_req_url().get('data').get('attributes').get('reputation')
        if rep is not None:
            return rep
        else:
            raise FileNotFoundError()

    def post_url(self) -> str:
        rep: str = self._post_req_url().get('data').get('type')
        if rep is not None:
            return rep
        else:
            raise FileNotFoundError()

    def post_get_url(self):
        self.post_url()
        for _ in range(10):
            print('Checking...')
            res_code = self._get_req_url().get('data').get('attributes').get('last_http_response_code')
            if res_code == 200:
                return self.get_url()
            else:
                time.sleep(30)
        raise vt_exeptions.EmptyContentError()



    def _get_req_file(self):
        pass

    def _post_req_file(self, password):
        pass
