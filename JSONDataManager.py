import json


class JsonData(object):

    def __init__(self,file_name):
        self._file_name = file_name

    #return dict or list
    def read_json_file(self):
        with open(self._file_name) as json_data:
            data = json.load(json_data)
            return data

    def get_value(self, key):
        data = self.read_json_file()
        return data[key]




