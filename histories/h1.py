from models import classes
from models import objects_m

class Search_brother:

    #spaces
    maison = classes.Space('maison')
    boutique = classes.Space('boutique')
    eglise = classes.Space('eglise')
    champs = classes.Space('champs')
    garage = classes.Space('garage')
    market = classes.Space('market')
    rod = classes.Space('rod')
    
    def __init__(self, player):
        self.doc_commands = {
            "stop" : "Command to stop game",
        }
        self.player = player
        self.stop_story = False
        self.maison.connection_auther_space([self.boutique,self.rod])
        self.rod.connection_auther_space([self.maison, self.boutique, self.eglise, self.champs, self.garage, self.market])
        self.eglise.connection_auther_space([self.rod, self.maison, self.garage])
        self.garage.connection_auther_space([self.rod, self.maison, self.market, self.boutique])
        self.boutique.connection_auther_space([self.rod, self.garage, self.market, self.eglise])
        self.market.connection_auther_space([self.rod, self.garage, self.champs, self.boutique])
        self.champs.connection_auther_space([self.rod, self.maison, self.market, self.boutique])
        
        action = objects_m.Instruction(name="pachemin",live=12)
        
        instruction = "Your Brother is on the market but you will fight one enemie on this space"
        action.make_instruction(instruction=instruction)
        self.garage.add_object([action])
        
        self.commands = {
            "stop" : lambda : self.stop(),
        }
        self.player.space.connection_auther_space([self.rod])
        for i, j in self.commands.items():
            self.player.commands[i] = j
        for i, j in self.doc_commands.items():
            self.player.doc_commands[i] = j
    
    def start(self, perso=None):
        print("You have back at your home and you find that your brother was kidnap:")
        self.explainations()
        self.player.show_doc_commands()
        while not self.stop_story:
            self.player.action(input("(position - {})Enter one command : ".format(self.player.position())))
    
    def stop(self):
        self.stop_story = True
    
    def explainations(self):
        input("You will find one object in all places this \n object should help you to find your brother (press enter to start game)")
        

