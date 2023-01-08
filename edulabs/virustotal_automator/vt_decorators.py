from vt_base import *
import time


class VTDecorators(VTAutomator):

    def cache_url(self, func):
        def wrapper(url):
            if url in self.__cache_url:
                result = self.__cache_url[url]
                last_analysis_date = result["last_analysis_date"]
                if (time.time() - last_analysis_date) < 86400:  # 86400 seconds = 1 day
                    return result
                else:
                    self.__cache_url.pop(url)
            result = func(url)
            self.__cache_url[url] = result
            return result

        return wrapper

    def cache_file(self, func):
        def wrapper(url):
            if url in self.__cache_file:
                result = self.__cache_file[url]
                last_analysis_date = result["last_analysis_date"]
                if (time.time() - last_analysis_date) < 86400:  # 86400 seconds = 1 day
                    return result
                else:
                    del self.__cache_file[url]
            result = func(url)
            self.__cache_file[url] = result
            return result

        return wrapper

    def _get_req_url(self):
        pass

    def _post_req_url(self):
        pass

    def _get_req_file(self):
        pass

    def _post_req_file(self, password):
        pass
