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


class JsonCsv:

    def __init__(self, csv_path: str, csv_delimiter, json_path: str):
        if not os.path.exists(json_path) or os.path.splitext(json_path)[1] != '.json':
            raise BadPathError()
        if os.path.exists(csv_path):
            raise PathExistError()

        self.__csv_delimiter: str = csv_delimiter
        self.__json_path: str = json_path
        self.__csv_path: str = csv_path

    def _get_content(self) -> list[dict]:
        try:
            with open(self.__json_path, 'r') as fh:
                content = list(json.load(fh))
            return content
        except Exception:
            print('Error')

    def json_to_csv(self) -> None:
        if not self._get_content():
            raise FileReaderError()
        if os.path.splitext(self.__csv_path)[1] == '.csv':
            end_string = ''
        else:
            end_string = '.csv'

        field_names = list(self._get_content()[0].keys())

        with open(f'{self.__csv_path}{end_string}', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, field_names, delimiter=self.__csv_delimiter)
            writer.writeheader()
            writer.writerows(self._get_content())


if __name__ == '__main__':
    csv_json: JsonCsv = JsonCsv(
        csv_path=r'test.csv',
        json_path=r'test.json',
        csv_delimiter=';'
    )

    csv_json.json_to_csv()
