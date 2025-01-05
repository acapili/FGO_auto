#Profile code to identify slow parts of the program
#python -m cProfile main.py


from user_config import user_config
from program_logic import program_logic
#only have this imported for testing purposes
from android_interface import android_interface

from color_sensing import color_sensing
from tap_coordinates import tap_coordinates

import time


def main():
    movement = android_interface()
    # Capture screenshot from the device

    #loading in data from JSON file
    existing_data =  user_config()
    files = existing_data.load_from_file()

    tapping_locations = tap_coordinates()

    # temp = color_sensing()

    # for x in range(5):
    #     tina = temp.get_max_rgb("refrences_for_game/card_picking.png", tapping_locations.get_card_box(x))
    #     print(tina)

    for x in range(3):
        logic = program_logic(files, x + 1)
        logic.servent_skill()
        logic.enemy_tap()
        logic.attack_tap()
        movement.capture_screenshot()
        logic.noble_tap()
        logic.select_cards()
        time.sleep(7)
        for z in range(3):
            movement.tap(tapping_locations.get_masters_face())
            time.sleep(0.3)
        time.sleep(19)

if __name__ == "__main__":
    main()