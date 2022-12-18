import json


class UserData:
    """
    connecting the json file with the user information
    for inserting user information and storing it
    checking for information and returning it
    """
    def __init__(self, directory: str, filename: str):
        self.__directory: str = directory
        self.__filename: str = filename

    def write_data(self, new_data: dict, dict_key: str,) -> None:
        with open(f"{self.__directory}/{self.__filename}", 'r+') as fh:
            # Load DB file
            file_data: json = json.load(fh)
            # append dict data to DB file
            if len(file_data[dict_key]) == 0:
                file_data[dict_key].append(new_data)
                # Sets file's current position at offset.
                fh.seek(0)
                # Convert back to Json
                print(file_data[dict_key])
                json.dump(file_data, fh, indent=4)
            else:
                for i in file_data[dict_key]:
                    if not list(i.keys()) in file_data[dict_key]:
                        file_data[dict_key].append(new_data)
                        # Sets file's current position at offset.
                        fh.seek(0)
                        # Convert back to Json
                        json.dump(file_data, fh, indent=4)
                        break
                    else:
                        raise KeyError("ALL READY IN USE!")


    def _get_data(self, data_key: str, dict_key: str,) -> dict:
        keys: list = []
        # load DB file
        with open(f"{self.__directory}/{self.__filename}", 'r+') as fh:
            file_data: dict = json.load(fh)
            # loop and if key is present return
            for place in file_data[dict_key]:
                keys.append(list(place.keys())[0])
                if data_key in keys:
                    return place
        # else return not found
        raise KeyError("ERROR! NOT FOUND")
