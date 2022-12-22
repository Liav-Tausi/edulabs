import json


def write_data(new_data: dict, dict_key: str, filename='db.json'):
    with open(filename, 'r+') as file:
        # Load DB file
        file_data = json.load(file)
        # append dict data to DB file
        if len(file_data[dict_key]) == 0:
            file_data[dict_key].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # Convert back to Json
            json.dump(file_data, file, indent=4)
        else:
            for i in file_data[dict_key]:
                print(list(new_data.keys())[0], file_data[dict_key][0])
                if not list(i.keys())[0] in file_data[dict_key][0]:
                    file_data[dict_key].append(new_data)
                    # Sets file's current position at offset.
                    file.seek(0)
                    # Convert back to Json
                    json.dump(file_data, file, indent=4)

                else:
                    print("EMAIL IS ALREADY IN USE.")


def get_data(data_key: str, dict_key: str, filename: str = 'db.json') -> dict:
    keys: list = []
    # load DB file
    with open(filename, 'r+') as file:
        file_data: dict = json.load(file)
        # loop and if key is present return
        for i in file_data[dict_key]:
            keys.append(list(i.keys())[0])
            if data_key in keys:
                return i
    # else return not found
    return {"ERROR": "NOT FOUND"}