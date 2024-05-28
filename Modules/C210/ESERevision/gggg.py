
class Character:
    def __init__(self, name, health, location):
        self.__name = name
        self.__health = health
        self.__location = location
        
    def move(self, direction):
        if direction == "north":
            self.__location += 10 # assuming movement is in steps of 10 for simplicity
        elif direction == "south":
            self.__location -= 10
        elif direction == "east":
            self.__location += 20
        elif direction == "west":
            self.__location -= 20
        
    def attack(self):
        print("Character attacks")
    
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def setHealth(self, points):
        if points >= 0: # ensure health doesn't go below zero
            self.__health = points
            
class Player(Character):
    def __init__(self, name, health, location):
        super().__init__(name, health, location)
        
    def take_damage(self, damage):
        if damage > 0: 
            self.__health -= damage
    
    def attack(self):
        print("Player attacks")
    
    def __str__(self):
        out_str = "Player" + self.getName 
        out_str += "\n" + "Current health points: " + self.getHealth
        return out_str
