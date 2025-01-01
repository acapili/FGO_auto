# takes the JSON file and parses through it
from android_interface import and_int
from tap_cordinates import Coordinates

class parser:
    tapping_function = and_int()
    tapping_locations = Coordinates()

    def __init__(self, json_data, number):
        self.turn_structure = json_data
        if number in {1,2,3}:
            placement = str(f"Turn{number}")
            self.turn = self.turn_structure[placement]

    # def servent_skill(self):

    def master_skills(self):
        if self.turn["master skills"] < 4 and not 0:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(self.turn["master skills"]))
        elif self.turn["master skills"] >= 4 and self.turn["master skills"] < 6:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            for x in range(self.turn["master skills"] - 2):
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(x))
        elif self.turn["master skills"] == 6:
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(2))
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(3))
        else:
            print("Error: master skills function or JSON file poorly written")


    def enemy_selction(self):
        if self.turn["enemy selection"] < 4 and not 0:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(self.turn["enemy selection"]))
        elif self.turn["enemy selection"] >= 4 and self.turn["enemy selection"] < 6:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            for x in range(self.turn["enemy selection"] - 2):
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(x))
        elif self.turn["enemy selection"] == 6:
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(2))
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(3))
        else:
            print("Error: enemy selection function poorly written or JSON file value is wrong")


    # def noble_phantasms(self):

    # def card_selection(self):


    # def battle_menu(self):
    #     if self.turn["battle menu"] == 1:
    #         self.tapping_function.tap(self.tapping_locations.get_battle_menu())

                