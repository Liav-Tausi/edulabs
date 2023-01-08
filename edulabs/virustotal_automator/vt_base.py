from abc import ABC, abstractmethod
from datetime import timedelta, date
import datetime
import time



class VTAutomator(ABC):
    # _____urls_api_____ #
    __GET_VT_API_URL: str = r'https://www.virustotal.com/api/v3/urls/'

    __POST_VT_API_URL: str = r'https://www.virustotal.com/api/v3/urls'

    # _____files_api_____ #
    __GET_VT_API_FILE: str = r'https://www.virustotal.com/api/v3/files/'

    __POST_VT_API_FILE: str = r'https://www.virustotal.com/api/v3/files'

    def __init__(self, ref_cache_month: int = 1):
        self.__requests_amount_limit: int = 500
        self.__requests_amount_limit_counter: int = 0

        self.__requests_per_minute_limit: int = 4
        self.__requests_per_minute_limit_counter = 0

        if ref_cache_month < 1:
            ref_cache_month = 1
        ref_date = date.today() + timedelta(weeks=4 * ref_cache_month)
        self.__ref_cache_month: date.month = ref_date.month

        self.__cache_url: dict = dict()
        self.__cache_file: dict = dict()

    # _____property_____ #

    @property
    def get_vt_api_url(self) -> str:
        return self.__GET_VT_API_URL

    @property
    def post_vt_api_url(self) -> str:
        return self.__POST_VT_API_URL

    @property
    def get_vt_api_file(self) -> str:
        return self.__GET_VT_API_FILE

    @property
    def post_vt_api_file(self) -> str:
        return self.__POST_VT_API_FILE

    @property
    def requests_amount_limit(self) -> int:
        return self.__requests_amount_limit

    @property
    def requests_amount_limit_counter(self) -> int:
        return self.__requests_amount_limit_counter

    @property
    def requests_per_minute_limit(self) -> int:
        return self.__requests_per_minute_limit

    @property
    def requests_per_minute_limit_counter(self) -> int:
        return self.__requests_per_minute_limit_counter

    # _____abstractmethod_urls____ #

    @abstractmethod
    def _get_req_url(self):
        pass

    @abstractmethod
    def _post_req_url(self):
        pass

    # _____abstractmethod_files____ #

    @abstractmethod
    def _get_req_file(self):
        pass

    @abstractmethod
    def _post_req_file(self, password):
        pass

    # _____setters_____#

    def set_amount_limit_counter(self) -> None:
        self.__requests_amount_limit_counter += 1

    def set_per_minute_limit_counter(self) -> None:
        self.__requests_amount_limit_counter += 1

    def set_amount_limit_refresh(self) -> None:
        day = datetime.timedelta(hours=24)
        while True:
            time.sleep(day.total_seconds())
            self.__requests_amount_limit_counter = 0

    def set_per_minute_limit_refresh(self) -> None:
        while True:
            time.sleep(60)
            self.__requests_amount_limit_counter = 0
