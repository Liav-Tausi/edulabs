import os
import json
import pprint


class DirDictError(Exception):
    pass


class PathNotFoundError(DirDictError):
    def __init__(self):
        super().__init__('Path not found.')


class DirDict:

    def __init__(self, directory_path: str, json_path: str = None):
        if not os.path.exists(directory_path):
            raise PathNotFoundError()

        self.__directory_path: str = directory_path
        self.__json_path: str = json_path

        self.__path_dict: dict = {
                    "dirs": [],
                    "files": []
        }

    def path_to_json(self) -> dict[str, str]:
        for root, dirs, files in os.walk(self.__directory_path):
            subdir = root.split(self.__directory_path)[-1]
            if subdir:
                subdir_dict = {
                    'dirs': [],
                    'files': []
                }

                for file in files:
                    subdir_dict['files'].append(file)

                for subdir in dirs:
                    sub_subdir_dict = {
                        'dirs': [],
                        'files': []
                    }
                    subdir_dict['dirs'].append({subdir: sub_subdir_dict})
                self.__path_dict[subdir] = subdir_dict

            if self.__json_path is not None:
                if os.path.splitext(self.__json_path)[1] == '.json':
                    end_string = ''
                else:
                    end_string = '.json'

                with open(f'{self.__json_path}{end_string}', 'w') as fh:
                    json.dump(self.__path_dict, fh)
        return self.__path_dict


if __name__ == '__main__':
    dir_dict: DirDict = DirDict(directory_path=os.path.dirname(os.path.dirname(__file__)), json_path='test2')
    pprint.pprint(dir_dict.path_to_json())
