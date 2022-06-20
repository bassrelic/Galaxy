"""This method defines technologies"""
import json
class Technology:
    """This class defines technologies"""
    def __init__(self, name, definition):
        self.name = name
        self.description = definition["description"]
        self.research = definition["research"]
        self.prereq = definition["prereq"]

    def get_name(self):
        """This method returns the name of this technologie"""
        return self.name

    def get_research(self):
        """This method returns the research cost of this technologie"""
        return self.research

    def get_prereq(self):
        """This method returns the prerequisite technologies"""
        return self.prereq

    def get_description(self):
        """This method returns the description of this technologie"""
        return self.description

    @classmethod
    def get_all_technology_list(cls):
        """This method generates a random beief with random intensity"""
        with open('src\\technology\\technologies.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
