"""This module defines the console"""
import pygame
from galaxy.planet.planet import Planet
from object.object import Object
import config

class ConsoleHandling():
    """This Class is used to hold information needed to process console commands"""
    def __init__(self) -> None:
        self.last_executed = 1
        self.new_command = False

    def new_command_ready(self):
        """This Method is used to acticate handling of newest command"""
        self.new_command = True

    def execute_last_command(self, commandlist, console, spriteslist):
        """This Method is used to execute the last command present in console and not already executed"""
        if len(commandlist) > self.last_executed and self.new_command is True:
            command=commandlist[self.last_executed].split(".")
            print(command)
            print(len(command))
            if command[0] == "$set" and len(command) >= 4:
                # Example command: set.hosp.earth.0.0 sets the hospitality of earth to 0%
                if command[1] == "hosp" and len(command) == 5:
                    # get entity name
                    name = command[2]
                    # get value
                    value = str(command[3] + "." + command[4])
                    for item in spriteslist:
                        if isinstance(item, Planet) and item.get_name().lower() == name:
                            item.set_hospitability(float(value))
                            retcommand = str(str(command) + "\n executed!")
                            console.write_text_to_console(retcommand)
            else:
                console.write_text_to_console("Unknown command!")

            self.new_command = False
            self.last_executed = self.last_executed + 2 # next line we are interested in is after console response

class Console(Object):
    """This class defines the console in terms of size and looks"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.c_h = ConsoleHandling()
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = pygame.display.get_window_size()[0]
        self.height = 300
        self.set_path()
        self.parent = None
        self.console_text_list = ["~~~This is the console, feel free to try stuff~~~","$"]

    def step(self):
        """This Method defines the step behaviour of the Console"""
        font = pygame.font.SysFont('Arial', 20)
        self.set_path()
        title_text = self.name
        text = font.render(str(title_text), True, config.WHITE)
        self.image.blit(text, (75, 10))
        y_pos_text = 40

        for element in self.console_text_list:
            writetext = element
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (125, y_pos_text))
            y_pos_text = y_pos_text + 25

    def write_char_to_console(self, text):
        """This method defines the write char to console behaviour"""
        list_length = len(self.console_text_list)
        if list_length > 1:
            prev_text = self.console_text_list.pop(list_length-1)
            if prev_text.startswith('$'):
                if len(prev_text) >= 1 and text != "\n":
                    self.console_text_list.append(str(prev_text + text))
                else:
                    self.console_text_list.append(prev_text)
                    self.c_h.new_command_ready()
                    self.console_text_list.append('$')
        else:
            self.console_text_list.append(str("$" + text))
        self._check_max_length()

    def write_text_to_console(self, text):
        """This method defines the write text to console behaviour"""
        list_length = len(self.console_text_list)
        if list_length > 2:
            prev_text = self.console_text_list.pop(list_length-1)
            cleaned_text = text.lstrip("$")
            self.console_text_list.append(str(prev_text + ">" + cleaned_text))
            self.console_text_list.append("$")
        else:
            self.console_text_list.append(str("$" + text))
            self.console_text_list.append("$")
        self._check_max_length()

    def handle_commands(self, spriteslist):
        """This method handles commands present in the console"""
        self.c_h.execute_last_command(self.console_text_list, self, spriteslist)

    def _check_max_length(self):
        """This method checks the length of console inputs and removes anything over limit"""
        if len(self.console_text_list) > 10:
            self.console_text_list.pop(1)
