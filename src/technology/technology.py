"""This method defines technologies"""
import json
class Technology:
    """This class defines technologies"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """This method returns the name of this technologie"""
        return self.name

    @classmethod
    def get_all_technology_list(cls):
        """This method generates a random beief with random intensity"""
        with open('src\\technology\\technologies.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
