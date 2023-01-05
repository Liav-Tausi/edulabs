import csv
import os


class FileReaderError(Exception):
    pass


class BadPathError(FileReaderError):
    def __init__(self):
        super().__init__('File not found.')


class CsvReading:

    def __init__(self, file_path: str, delimiter: str = ','):
        if not os.path.exists(file_path) or os.path.splitext(file_path)[1] != '.csv':
            raise BadPathError()
        self.__file_path: str = file_path
        self.__delimiter: str = delimiter

    def _get_content(self):
        try:
            with open(self.__file_path, 'r') as fh:
                rows_list: list = list()
                for row in csv.DictReader(fh, delimiter=self.__delimiter):
                    rows_list.append(row)
                return rows_list
        except Exception:
            print('Reading Error')

    def columns(self):
        return len(self._get_content()[0].keys())

    def rows(self):
        return len(self._get_content()) + 1


if __name__ == '__main__':
    csv_reading: CsvReading = CsvReading(
        r'C:\Users\liavt\PycharmProjects\LernningPython\edulabs\exercises\files_ex\practise_folder2\usernames.csv')
    print(csv_reading.columns())
    print(csv_reading.rows())

