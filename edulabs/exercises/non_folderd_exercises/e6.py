from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait
import concurrent
import time
import requests


# 1 Write a program that receives a number of seconds from a user and counts down this amount of seconds
# in resolution of 0.1 second by printing the amount of time left.
# For example, if the user inserts 3, your program should constantly print:
# 3 seconds left
# 2.9 seconds left
# 2.8 seconds left
# 2.7 seconds left
# ….
# 0.1 seconds left
# DONE!

class CounterOne:

    def __init__(self, time_: str = 10):
        self.__time_: int = datetime.strptime(time_, '%S').second

    def counting_one(self) -> None:
        now: int = datetime.utcnow().second
        fut: int = now + self.__time_
        while fut >= now:
            time.sleep(0.1)
            self.__time_ -= 0.1
            print(round(self.__time_, 1))
            if int(self.__time_) <= 0:
                print('Done')
                quit()

#
# if __name__ == '__main__':
#     CounterOne('3').counting_one()


# 2 Change your previous program in the following way: after every second you should send an api request to kanye API (https://kanye.rest/)
# that on each request returns one of kanye west tweets and prints the result. Now, here comes the catch
# - make sure the counting is not slowed down or skipped because of sending requests to this api. Hint: user multi-threading :)

class CounterTwoExeptions(Exception):
    pass


class RequestsError(CounterTwoExeptions):
    pass


class CounterTwo:

    def __init__(self, path_: str = 'https://api.kanye.rest//', time_s: int = 10, max_workers: int = 4):
        self.__time_s: int = datetime.strptime(str(time_s), '%S').second
        self.__path_: str = path_
        self.__max_workers: int = max_workers

    def content(self):
        req: 'requests' = requests.get(self.__path_)
        req_content: dict = req.json()["quote"]
        if req.status_code > 400:
            raise RequestsError(f"Status code is {req.status_code}.")
        print(req_content)

    def counting_two(self) -> None:
        executor = ThreadPoolExecutor(max_workers=self.__max_workers)
        now: int = datetime.utcnow().second
        fut: int = now + self.__time_s
        futures: list = list()
        while fut > now:
            if int(fut) == round(fut, 1):
                futures.append(executor.submit(self.content))
            fut -= 1
            time.sleep(1)
        print("DONE!")
        done, not_done = wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
        print(len(done))
        print(len(not_done))



if __name__ == '__main__':
    CounterTwo(time_s=3).counting_two()
