import csv
import json
import os


class FileReaderError(Exception):
    pass


class BadPathError(FileReaderError):
    def __init__(self):
        super().__init__('File not found.')


class PathExistError(FileReaderError):
    def __init__(self):
        super().__init__('File already exists.')


class FileEmptyError(FileReaderError):
    def __init__(self):
        super().__init__('CSV file is empty.')


class CsvJson:

    def __init__(self, csv_path: str, csv_delimiter, json_path: str):
        if not os.path.exists(csv_path) or os.path.splitext(csv_path)[1] != '.csv':
            raise BadPathError()
        if os.path.exists(json_path):
            raise PathExistError()

        self.__csv_delimiter: str = csv_delimiter
        self.__json_path: str = json_path
        self.__csv_path: str = csv_path

    def _get_content(self) -> list[dict]:
        try:
            with open(self.__csv_path, 'r') as fh:
                content = list(csv.DictReader(fh))
            return content
        except Exception:
            print('Error')

    def csv_to_json(self) -> None:
        rows: list = list()
        content = self._get_content()
        if not content:
            raise FileReaderError()
        if os.path.splitext(self.__json_path)[1] == '.json':
            end_string = ''
        else:
            end_string = '.json'

        with open(f'{self.__json_path}{end_string}', 'w') as fh:
            column_names = str(content[0].keys()).split(self.__csv_delimiter)
            for row in content:
                row_names = str(row.values()).split(self.__csv_delimiter)
                row_dict: dict = dict()
                for index, column_name in enumerate(column_names):
                    row_dict[column_name] = row_names[index]
                rows.append(row_dict)
            json.dump(rows, fh)


if __name__ == '__main__':
    csv_json: CsvJson = CsvJson(
        csv_path=r'C:\Users\liavt\PycharmProjects\LernningPython\edulabs\exercises\files_ex\practise_folder2\usernames.csv',
        json_path=r'test', csv_delimiter=';')
    csv_json.csv_to_json()
