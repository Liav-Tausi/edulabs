"""
FileInterpreter is a tool that allows users to read and manipulate different types of files,

                        such as CSV, TXT and JSON files .

The FileInterpreter uses inheritance and polymorphism to implement the different file types

created by: liav tausi
date: 2022/12/13

"""

from abc import ABC, abstractmethod
import csv
import os
import json


class BaseFile(ABC):

    def __init__(self, path: str):
        if not os.path.exists(path):
            raise Exception()
        if os.path.splitext(path)[-1][1:] not in self._extension():
            raise Exception()
        self._path: str = path

    def __add__(self, other):
        # check if files are of the same type
        if self._path[-3:] != other._path[-3:]:
            raise ValueError('Cannot combine files of different types')
        # check if files are txt or csv one is enghth
        allowed = ["csv", "txt"]
        if self._path[-3:] not in allowed:
            raise ValueError('Cannot combine files that are not csv or txt')
        # create new file path
        new_path = os.path.join(os.path.dirname(self._path),
                                f"{os.path.basename(self._path)}_{os.path.basename(other._path)}")
        # check if new file already exists
        if os.path.exists(new_path):
            raise FileExistsError('File with this name already exists')
        # combine contents of txt files
        if self._path[-3:] == "txt":
            with open(new_path, 'w') as fh:
                fh.write(self.content() + other.content())
        # combine contents of csv files
        else:
            # check for different fieldnames
            with open(self._path, "r") as fh1:
                # sniffing for the delimiters
                delimiter_detect1 = csv.Sniffer().sniff(fh1.read(1024))
                delimiter1 = delimiter_detect1.delimiter
                # reset the file pointers to the beginning of the files after sniffing for the delimiters
                fh1.seek(0)
                reader1 = csv.DictReader(fh1, delimiter=delimiter1)
                fieldnames1 = reader1.fieldnames

            with open(other._path, "r") as fh2:
                delimiter_detect2 = csv.Sniffer().sniff(fh2.read(1024))
                delimiter2 = delimiter_detect2.delimiter
                fh2.seek(0)
                reader2 = csv.DictReader(fh2, delimiter=delimiter2)
                fieldnames2 = reader2.fieldnames

            if delimiter1 != delimiter2:
                CsvFile(self._path)._delimiter = ","
            if fieldnames1 != fieldnames2:
                raise ValueError('Cannot combine csv files with different fieldnames')

            # create new file with the fieldnames of the first file
            with open(new_path, "w", newline="") as new_file:
                dict_writer = csv.DictWriter(new_file, fieldnames1, delimiter=CsvFile(self._path)._delimiter)
                dict_writer.writeheader()
                # open first file and insert content to new file
                with open(self._path, "r") as fh1:
                    reader1 = csv.DictReader(fh1)
                    for row in reader1:
                        dict_writer.writerow(row)
                # open second file and insert content to new file
                with open(self._path, "r") as fh2:
                    reader2 = csv.DictReader(fh2)
                    for row in reader2:
                        dict_writer.writerow(row)


    def file_size(self) -> int:
        """
        This method returns the size of the file in bytes.
        :return: int
        """
        file_stats = os.stat(self._path)
        return file_stats.st_size

    def file_size_unit(self, unit: str = None) -> float:
        """
         converts the file size to a different unit, such as megabytes or gigabytes.
         The unit to convert to must be specified as an argument to the method.
         If no unit is specified, the method returns the size of the file in bytes by default.
        :param unit:
        :return: float
        """
        if unit is None:
            return self.file_size()
        elif unit == "megabytes":
            return self.file_size() / (1024 * 1024)
        elif unit == "gigabytes":
            return self.file_size() / (1024 ** 3)
        elif unit == "terabytes":
            return self.file_size() / (1024 ** 4)
        else:
            return self.file_size()

    def _get_content(self) -> list:
        with open(self._path, "r") as fh:
            content = self._specific_content(fh)
        return content

    @abstractmethod
    def _specific_content(self, fh):
        pass

    @abstractmethod
    def content(self):
        pass

    @abstractmethod
    def _extension(self):
        pass


class CsvFile(BaseFile):
    """
    this class provides support for reading and manipulating delimited CSV files.
    such as access individual rows, columns, or cells in the CSV file
    """

    def __init__(self, path: str, delimiter: str = ","):
        super().__init__(path)
        self._delimiter: str = delimiter

    def _extension(self) -> str:
        return "csv"

    def _specific_content(self, fh) -> list[dict]:
        row_list: list = list()
        for row in csv.DictReader(fh, delimiter=self._delimiter):
            row_list.append(row)
        return row_list

    # get the files delimiter
    def delimiter(self) -> str:
        return self._delimiter

    # get the files content
    def content(self) -> list[dict]:
        return self._get_content()

    # get the amount of rows
    def rows(self) -> int:
        num_rows: int = 0
        for row in self._get_content():
            num_rows += 1
        return num_rows

    # get the amount of columns
    def columns(self) -> int:
        num_columns: int = 0
        for row in self._get_content():
            num_columns = max(num_columns, len(row))
        return num_columns

    # get a specific row
    def by_row(self, row_num: int) -> dict:
        content = list(self.content())
        content.insert(0, "")
        content.insert(0, "")
        if row_num >= len(content):
            raise IndexError("Row index out of range")
        row = content[row_num]
        if len(row) == 0:
            return {}
        keys = row.keys()
        if len(keys) == 0:
            for idx, val in enumerate(row):
                return {str(idx): val}
        else:
            return row

    # get a specific column starting from index 0
    def by_column(self, column_num: int) -> list:
        column_values = []
        content = self.content()
        if len(content) == 0:
            return list()
        if column_num >= len(content[0]):
            raise IndexError("Column index out of range")
        keys = list(content[0].keys())
        for row in content:
            column_values.append(row[keys[column_num]])
        return column_values

    # get a specific value in file with indx row and index column
    def by_cell(self, row_num: int, column_num: int) -> str:
        content = self.content()
        if len(content) == 0:
            raise Exception("Empty file")
        if column_num >= len(content[0]):
            raise IndexError("Column index out of range")
        if row_num >= len(content):
            raise IndexError("Row index out of range")
        keys = list(content[0].keys())
        if len(keys) == 0:
            return content[row_num][column_num]
        return content[row_num][keys[column_num]]


class JsonFile(BaseFile):
    """
    class for reading and getting statistics about the contents of a JSON file
    """
    def _extension(self) -> str:
        return "json"

    def _specific_content(self, fh):
        return json.load(fh)

    # get the files content
    def content(self):
        return self._get_content()

    # True if json is a list
    def is_list(self) -> bool:
        if isinstance(self.content(), list):
            return True
        else:
            return False

    # True if json is an object
    def is_object(self) -> bool:
        if isinstance(self.content(), dict):
            return True
        else:
            return False


class TxtFile(BaseFile):
    """
    class for reading and getting statistics about the contents of a TXT file
    """

    def __init__(self, path: str, read_amount: int = None):
        super().__init__(path)
        self.read_amount: int = read_amount

    def _extension(self) -> str:
        return "txt"

    def _specific_content(self, fh) -> list[str]:
        return fh.read()

    # get the files content
    def content(self) -> list[str]:
        return self._get_content()

    # get the amount of words "separated by whitespace"
    def words_amount(self) -> int:
        return len(str(self.content()).split())

    # get the avg amount of characters word
    def avg_word_len(self) -> float:
        total_length = 0
        if self.content() == 0:
            raise Exception("empty file")
        for word in str(self.content()).split():
            total_length += len(word)
        avg_word_len = total_length / len(str(self.content()).split())
        return avg_word_len


if __name__ == "__main__":
    csv_file1 = CsvFile("FHfiles/email-password-recovery-code.csv", ";")
    csv_file2 = CsvFile("FHfiles/csv_combine_test.csv", ",")
    json_file = JsonFile("FHfiles/json_ex.json")
    json_file2 = JsonFile("FHfiles/json_ex2.json")
    txt_file1 = TxtFile("FHfiles/alice_in_wonderland.txt")
    txt_file2 = TxtFile("FHfiles/alice_in_wonderland2.txt")
    txt_file3 = TxtFile("FHfiles/alice_in_wonderland.txt_alice_in_wonderland2.txt")

    # json_file1 + json_file2
    # print(csv_file2.delimiter())
    # print(csv_file1.delimiter())
    # csv_file2 + csv_file1

    # files = [csv_file1, json_file1, txt_file1]
    # for i in files:
    #     print(i.content())

    # print(csv_file1.file_size())
    # print(csv_file1.file_size_unit("terabytes"))
    # print(csv_file1.columns())
    # print(csv_file1.rows())
    # print(csv_file1.by_row(6))
    # print(csv_file1.by_column(3))
    # print(csv_file1.by_cell(0, 3))

    # print(txt_file1.avg_word_len())
    # print(json_file.is_list())
    # print(json_file.is_object())
    # print()
    # print(txt_file2.words_amount()+txt_file1.words_amount())
    # print(txt_file3.words_amount())




