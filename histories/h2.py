import os
from models import classes
from models import objects_m

class Search_Mother:

    #spaces
    house = classes.Space('house')
    boutique = classes.Space('boutique')
    eglise = classes.Space('eglise')
    champs = classes.Space('champs')
    garage = classes.Space('garage')
    market = classes.Space('market')
    street = classes.Space('street')
    east = classes.Space(name='east', description="This space contained one \"enmie\" you should beat him to save your \"Mother\" ")
    
    def __init__(self, player):
        self.doc_commands = {
            "stop" : "Command to stop game",
            "instrutions" : "Command to see the instrutions when are in the house",
        }
        self.commands = {
            "stop" : lambda : self.stop(),
            "instrutions" : lambda : self.explainations(), 
        }

        self.player = player
        self.stop_story = False
        self.house.connection_auther_space([self.street])
        self.street.connection_auther_space([self.house, self.boutique, self.eglise, self.champs, self.garage, self.market, self.east])
        self.eglise.connection_auther_space([self.street, self.house, self.garage])
        self.garage.connection_auther_space([self.street, self.house, self.market, self.boutique])
        self.boutique.connection_auther_space([self.street, self.garage, self.market, self.eglise, self.east])
        self.market.connection_auther_space([self.street, self.garage, self.champs, self.boutique])
        self.champs.connection_auther_space([self.street, self.house, self.market, self.boutique])
        self.east.connection_auther_space([self.street, self.house, self.market])
        
        #liste of objects
        #maison
        dir_in = os.getcwd()
        table = objects_m.Instruction(name="table", live=12,description_object="a table", path=dir_in+"/models/table.txt")
        chair = objects_m.Instruction(name="chair", live=12, description_object="A chair", path=dir_in+"/models/chair.txt")
        floor = objects_m.Instruction(name="floor", live=12, description_object="Nothing importante", path=dir_in+"/models/floor.txt")        
        broken_necklace = objects_m.Instruction(name="broken_necklace", live=12, description_object="It is your mother's necklace strangely broken on the floor", path=dir_in+"/models/broken_necklace.txt")
        self.house.add_object([table, chair, floor, broken_necklace])
        
        #street
        perso = classes.Character(name="Neigbour",description_perso="It is your neigbour he says that a bunch of men came and kidnapped your mother. The went toward the east")
        self.street.add_perso([perso])
        
        #east the space where his mother is
        #enemie on this place
        enemie1 = classes.Enemie(name="enemie1", description_perso="that people have your mother", live=15, p_attack=5, path=dir_in+"/models/enemie1.txt")
        self.east.add_enemie([enemie1])
        
        self.player.move_to_space(self.house)
        self.player.know_story(self)        

        self.player.space.connection_auther_space([self.street])
        for i, j in self.commands.items():
            self.player.commands[i] = j
        for i, j in self.doc_commands.items():
            self.player.doc_commands[i] = j
    
    def start(self, perso=None):
        dir_in = os.getcwd()
        fiche = open(dir_in+"/models/house1.txt")
        for e in fiche.readlines():
            print(e)
        fiche.close()
        print("type \"commands\" to see all commands")
        print("")
        print("type \"instrutions\" to see instructions ")
        while not self.stop_story:
            self.player.action(input("(position - {})Enter a command : ".format(self.player.position())))
    
    def stop(self):
        self.stop_story = True
    
    def explainations(self):
        print("      You have borrowed money from a guy and then you backed the money late. the guy was angry,")
        print("and asked you interests, you refuse to give those interests, then guy try to oblige you ")
        print("to defend yourself you beat him up. Today you backed at home but you can find your mother ")
        print("inside. ")
        
        print("You are in the house type \"look\" to investigate :")
        #input("You will find one object in all places this \n object should help you to find your brother (press enter to start game)")
        

