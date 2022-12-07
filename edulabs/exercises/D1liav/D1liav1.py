import os
import csv


# class FileSearch:
#
#     def __init__(self, main_directory: str):
#         self.__main_directory: str = main_directory

#
#     def display_main_directory(self):
#         for root, dirs, files in os.walk(self.__main_directory):
#             print(root, files)
#
#
#     def __get_file(self, directory: str, name: str, type: str = None):
#         for root, dirs, files in os.walk(self.__main_directory):
#             for file in files:
#                 if file == name:
#                     with open(f"{self.__main_directory}/{directory}/{file}","r") as fh:
#                         if type == "columns":
#                             return fh.readline()
#                         if type == "rows":
#                             reader = csv.reader(fh)
#                             no_lines = len(list(reader))
#                             return no_lines
#                         return fh.read()
#
#
#     def amount_of_columns(self, directory: str, name: str) -> int:
#         file_details = self.__get_file(directory, name, "columns")
#         first_line = file_details
#         file = first_line.count(";")
#         return file + 1
#
#
#     def amount_of_rows(self, directory: str, name: str) -> int:
#         file_details = self.__get_file(directory, name, "rows")
#         return file_details



# if __name__ == "__main__":
    # file_search = FileSearch("files_ex")
    # file_search.display_main_directory()
    # print(file_search.amount_of_columns("practise_folder1", "access-code.csv"))
    # print(file_search.amount_of_rows("practise_folder2", "usernames.csv"))


