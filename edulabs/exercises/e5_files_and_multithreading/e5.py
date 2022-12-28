import os
import csv
import concurrent
import time
from e5_exeptions import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait


class CsvThread:
    def __init__(self, path: str, delimiter: str = ",", workers: int = 4):
        if os.path.splitext(path)[-1][1:] not in ['csv']:
            raise UnExceptableFile(path)
        if not os.path.exists(path):
            os.makedirs(path)

        self.__workers: 'ThreadPoolExecutor' = ThreadPoolExecutor(workers)
        self.__path: str = path
        self.__delimiter: str = delimiter
        self.__futures: list = list()


    @staticmethod
    def calculate_averages(data) -> 'dict[any, float]':
        averages: dict = dict()
        for key in data[0].keys():
            if key == 'Date':
                continue
            sum_of: int = 0
            count: int  = 0
            for line in data:
                sum_of += float(line[key])
                count += 1
            averages[key] = sum_of / count
        return averages


    def get_years(self) -> 'list[int]':
        with open(self.__path, 'r') as f:
            years_set: set = set()
            reader = csv.DictReader(f, delimiter=self.__delimiter)
            for line in reader:
                date = datetime.strptime(line['Date'].split('-')[2], "%Y").year
                years_set.add(date)
            return sorted(years_set)


    def write_yearly_file(self, year, year_data) -> 'None':
        with open(f'e5_files_endpoint/AAPL_{year}.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=year_data[0].keys(), delimiter=self.__delimiter)
            writer.writeheader()
            for line in year_data:
                writer.writerow(line)
            writer.writerow(self.calculate_averages(year_data))


    def create_yearly_files(self) -> 'None':
        if os.path.exists('e5_files_endpoint'):
            raise DirectoryAndFilesExist('Dir and files Already exists. delete "e5_files_endpoint" directory')
        else:
            if not os.path.exists('e5_files_endpoint'):
                os.makedirs('e5_files_endpoint')
            with open(self.__path, 'r') as fh:
                for year in self.get_years():
                    fh.seek(0)
                    reader = csv.DictReader(fh, delimiter=self.__delimiter)
                    year_data: list = list()
                    for line in reader:
                        date = datetime.strptime(line['Date'], "%d-%m-%Y").year
                        if date == year:
                            year_data.append(line)
                    self.__futures.append(self.__workers.submit(self.write_yearly_file, year, year_data))
            done, not_done = wait(self.__futures, return_when=concurrent.futures.ALL_COMPLETED)
            print(f"done: {len(done)}")
            print(f"not done: {len(not_done)}")


if __name__ == '__main__':
    try:
        csv_thread: 'CsvThread' = CsvThread(path='e5_files/apple_stock.csv', delimiter=',', workers=6)
        start = time.perf_counter()
        csv_thread.create_yearly_files()
        end = time.perf_counter()
        print(f"time took: {end - start} seconds")

    except UnExceptableFile:
        print('file not csv')

    except DirectoryAndFilesExist:
        print("dir and files already exists")
        quit()

    except Exception:
        print("Error")
