import os


class FileReaderError(Exception):
    pass


class BadPathError(FileReaderError):
    def __init__(self):
        super().__init__('File not found.')


class EndLineError(FileReaderError):
    def __init__(self):
        super().__init__('End line should be smaller then Start line.')


class EndLineNotViableError(FileReaderError):
    def __init__(self):
        super().__init__('End line larger then amount of words.')


class FileReader:

    def __init__(self, file_path: str, start_line: int = 0, end_line: int = None):
        if not os.path.exists(file_path) or os.path.splitext(file_path)[1] != '.txt':
            raise BadPathError()
        if not isinstance(start_line, int) and not isinstance(end_line, int):
            raise ValueError()
        elif start_line > end_line:
            raise EndLineError()

        self.__file_path: str = file_path
        self.__start_line: int = start_line
        self.__end_line: int = end_line

    def read_file(self) -> str:
        try:
            with open(self.__file_path, 'r') as fh:
                lines = fh.readlines()
                if self.__end_line is None:
                    self.__end_line = len(lines)
                if self.__end_line > len(lines):
                    raise EndLineNotViableError()
                return ''.join(lines[self.__start_line:self.__end_line])
        except Exception:
            print('Reading Error')


if __name__ == '__main__':
    abs_path = r'C:\Users\liavt\PycharmProjects\LernningPython\edulabs\file_handler\f_h_files\alice_in_wonderland.txt'
    file_reader: FileReader = FileReader(abs_path, 2, 6)
    print(file_reader.read_file())
