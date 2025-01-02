#Profile code to identify slow parts of the program
#python -m cProfile main.py


from user_config import CONFIG
from program_logic import parser
#only have this imported for testing purposes
from android_interface import and_int


def main():
    movement = and_int()
    # # Capture screenshot from the device
    # movement.capture_screenshot()
    movement.analyze_screen()
    #loading in data from JSON file
    existing_data =  CONFIG()
    files = existing_data.load_from_file()


    logic = parser(files, 1)
    logic.servent_skill()

if __name__ == "__main__":
    main()