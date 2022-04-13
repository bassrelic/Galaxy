"""This module implements stars / suns"""

from random import randint
from galaxy.planet.planet import Planet


class Star(Planet):
    """This class implements stars / suns"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.min_temp = randint(1726, 199727)
        self.path = self.__get_star_color_by_temp()
        self.width = 100
        self.height = 100
        self.set_path()
        diameter = -2
        while diameter <= 0:
            diameter = int(randint(20, 2000000000))
        self.set_diameter(diameter)
        # temperature range according to Harvard spectral classification (200000k assumed as upper limit)

    def __get_star_color_by_temp(self):
        """Generate path to star image by temperature"""
        temp_ranges = (3427, 4927, 5727, 7227, 9727, 30000, 2000000000)
        path_specific = ('M', 'K', 'G', 'F', 'A', 'B', 'O')
        path = "res\\planets\\stars\\star_"
        i = 0
        for temprange_upper in temp_ranges:
            if temprange_upper > self.min_temp:
                path = path + path_specific[i] + ".png"
                return str(path)
            i = i + 1
        return None

    def get_hospitability(self):
        """Overriding Planet method because stars are not hospitable"""
        return None

    def get_atmosphere(self):
        """Overriding Planet method because stars have mo atmosphere to speak of"""
        return None

    def get_dataslate_data(self):
        """This method returns a dict containing the necessairy data for the corresponding dataslate"""

        dataslate_data = {
            "Name"          : self.name,
            "temp"          : str(self.min_temp) + " °C",
            "diameter"      : str(self.diameter) + " km",
        }

        return dataslate_data

    def set_atmosphere(self, atmosphere):
        """Overriding Planet method because stars have mo atmosphere to speak of"""
        raise NotImplementedError('No atmosphere on Stars')

    def set_hospitability(self, hospitability):
        """Overriding Planet method because stars are not hospitable"""
        raise NotImplementedError('No hospitality value on a Star')

    def add_civilization(self, civilization):
        """Overriding Planet method because stars are unlikely to house a civilization"""
        raise NotImplementedError('No civilizations on a Star')
