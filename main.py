#Profile code to identify slow parts of the program
#python -m cProfile main.py


from user_config import CONFIG
from program_logic import parser


def main():
    #loading in data from JSON file
    existing_data =  CONFIG()
    files = existing_data.load_from_file()


    logic = parser(files, 1)
    logic.master_skills()
    logic.enemy_selction()



if __name__ == "__main__":
    main()