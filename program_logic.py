# takes the JSON file and parses through it
from android_interface import and_int
from tap_cordinates import Coordinates
import time

class parser:
    tapping_function = and_int()
    tapping_locations = Coordinates()

    def __init__(self, json_data, number):
        self.turn_structure = json_data
        if number in {1,2,3}:
            placement = str(f"Turn{number}")
            self.turn = self.turn_structure[placement]

    def servent_skill(self):
         for x in range(3):
            for y in range(3):
                if self.turn["skills"][x][y] > 1 and self.turn["skills"][x][y] < 5:
                    self.tapping_function.tap(self.tapping_locations.get_skills_coordinates(x, y))
                    time.sleep(0.5)
                    self.tapping_function.tap(self.tapping_locations.get_servent_skill_selection(self.turn["skills"][x][y] - 2))
                    for z in range(3):
                        self.tapping_function.tap(self.tapping_locations.get_masters_face())
                        time.sleep(0.3)
                elif self.turn["skills"][x][y] == 1:
                    self.tapping_function.tap(self.tapping_locations.get_skills_coordinates(x, y))
                    for z in range(3):
                        self.tapping_function.tap(self.tapping_locations.get_masters_face())
                        time.sleep(0.3)
                # else:
                #     print("skill not used")




    def funcitonal_taps(self, type):
        if self.turn[type] < 4 and not 0:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(self.turn[type]))
        elif self.turn[type] >= 4 and self.turn[type] < 6:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            for x in range(self.turn[type] - 2):
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(x))
        elif self.turn[type] == 6:
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(1))
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(2))
        else:
            print(f"Error: {type} function or JSON file poorly written")


    # def card_selection(self):

    # def battle_menu(self):

                