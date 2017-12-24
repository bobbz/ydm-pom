import json


class JsonDataManager():

    def __init__(self):

        pass

    def read_json_file(path):
        with open(path) as json_data:
            data = json.load(json_data)
            return data
