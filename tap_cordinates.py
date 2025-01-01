class Coordinates:
    def __init__(self):
        self.skills = {'x': [187, 660, 1137], 'y': 840}
        self.okay_button = [1500, 632]
        self.battle_menu = [2113, 311]
        self.master_skills_button = [2113, 469]
        self.master_skills_selection = {'x': [1880, 1930, 1980], 'y': 469}
        self.enemy_selection = {'x': [183, 556, 931], 'y': 65}
        self.masters_face = [2095, 97]
        self.noble_phantasms = {'x': [830, 1201, 1552], 'y': 270}
        self.servent_skill_selection = {'x': [690, 1160, 1552], 'y': 580}
        self.card_selction = {'x': [400, 776, 1200, 1550, 1940], 'y': 725}
        self.enemy_selection = {'x': [183, 556, 931], 'y': 65}


    def get_coordinates(self, category, number):
        if number < 0 or number > 5:
            print("invalid input for coordinate number")
            return None
        if category in self.__dict__:
            coords = self.__dict__[category]
            if 'x' in coords and 'y' in coords:
                x = coords['x'][number] if number <= len(coords['x']) else None
                y = coords['y']
                if x is not None:
                    return (x,y)
            else:
                print("the coords seem to be messed up")
        print("invalid input for category")
        return None

        
    def get_skills_coordinates(self, id, number):
        """Returns the (x, y) coordinates for the skill tap"""
        if id in {1, 2, 3} and number in {1, 2, 3}:
            x = self.skills['x'][id - 1] + (number - 1) * 130
            y = self.skills['y']
            return (x, y)
        else:
            print("Please enter a valid ID [1-3] and number [1-3]")
            return None
        
    def get_noble_phantasm(self, number):
        return self.get_coordinates("servent_skill_selection", number)
        
    def get_servent_skill_selection(self, number):
        return self.get_coordinates("servent_skill_selection", number)
        
    def get_enemy_selection(self, number):
        return self.get_coordinates("enemy_selection", number)
        
    def get_master_skills(self):
        return(self.master_skills_button[0], self.master_skills_button[1])
    
    def get_master_skills_selection(self, number):
        return self.get_coordinates("master_skills_selection", number)
    
    def get_battle_menu(self):
        return(self.battle_menu[0], self.battle_menu[1])
    
    def get_okay_button(self):
        return(self.okay_button[0], self.okay_button[1])
    
    def get_masters_face(self):
        return(self.masters_face[0], self.masters_face[1])
    
