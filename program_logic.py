# takes the JSON file and parses through it
from android_interface import android_interface
from tap_coordinates import tap_coordinates
from color_sensing import color_sensing
import time

class program_logic:
    tapping_function = android_interface()
    tapping_locations = tap_coordinates()
    color = color_sensing()

    def __init__(self, json_data, number):
        self.image_path = "screenshot.png"
        self.turn_structure = json_data
        if number in {1,2,3}:
            placement = str(f"Turn{number}")
            self.turn = self.turn_structure[placement]

    def servent_skill(self):
         """looking at a 2D array if it sees something higher than one it selects the skill 
         and appropriate servent. Zero means skill not used and 1 means simply tapping the button"""
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
                else:
                    print("skill not used")


    def master_taps(self):
        """Taking in a str(type) you can select masters any of the master skills """
        type = "master_skills"
        if self.turn[type] < 4 and self.turn[type] != 0:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(self.turn[type] - 1))
        elif self.turn[type] >= 4 and self.turn[type] < 6:
            self.tapping_function.tap(self.tapping_locations.get_master_skills())
            for x in range(self.turn[type] - 2):
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(x))
        elif self.turn[type] == 6:
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(1))
                self.tapping_function.tap(self.tapping_locations.get_master_skills_selection(2))
        else:
            print(f"Error: {type} function or JSON file poorly written")


    def enemy_or_noble_taps(self, type, function):
        """Logic for selecting either a enemy or a noble phantasm """
        if self.turn[type] < 4 and self.turn[type] != 0:
            self.tapping_function.tap(function(self.turn[type] - 1))
        elif self.turn[type] in {4,5}:
            for x in range(self.turn[type] - 2):
                self.tapping_function.tap(function(x))
        elif self.turn[type] == 6:
                self.tapping_function.tap(function(1))
                self.tapping_function.tap(function(2))
        else:
            print(f"Error: {type} function or JSON file poorly written")

    def enemy_tap(self):
        self.enemy_or_noble_taps("enemy_selection", self.tapping_locations.get_enemy_selection)

    def noble_tap(self):
        self.enemy_or_noble_taps("noble_phantasms", self.tapping_locations.get_noble_phantasm)


    def select_cards(self):
        """Given the type of card (0 = buster, 1 = quick, 2 = arts) that is needed it will output the first instances of that card type as a list
        depending on what noblephantasms are used"""
        if self.turn["noble_phantasms"] < 6 and self.turn["noble_phantasms"] > 3:
            z = 1
        elif self.turn["noble_phantasms"] <= 3:
            z = 2
        elif self.turn["noble_phantasms"] ==0:
            z = 3
        else:
            print("Invalid number of attacks given")
            return None
        
        y = 0
        list = []
        while len(list) < z and y != 5:
            temp = self.color.get_max_rgb(self.image_path, self.tapping_locations.get_card_box(y))
            if temp == self.turn["card_selection"]:
                list.append(y)         
            y = y + 1

        if len(list) != z:
            print("not enough cards of selected type found")
            for a in range(3):
                self.tapping_function.tap(self.tapping_locations.get_cards(a))
                time.sleep(0.3)
        else:
            for a in range(len(list)):
                self.tapping_function.tap(self.tapping_locations.get_cards(list[a]))
                time.sleep(0.3)

    def attack_tap(self):
        self.tapping_function.tap(self.tapping_locations.get_attack_button())
        time.sleep(0.5)


    # def compiled_taps(self):
    #     self.servent_skill()
    #     self.enemy_tap()
    #     self.attack_tap()
    #     self.noble_tap()
    #     self.select_cards()

    


    # def card_selection(self):

    # def battle_menu(self):

                