import os

class Object:
    
    def __init__(self, player=None, name="", time=0, live=0, description_object="", path=""):
        self.name = name
        self.path = path
        self.image = "image"
        self.time = time
        self.live = live
        self.player = player
        self.doc_commands = {}
        self.commands = {}
        self.description_object = description_object
        
        if self.player:
            self.connect_player()
    
    def decrease_live(self):
        pass
    
    def object_carac(self):
        pass
    
    def list_caracteristiques(self):
        print("name : {} ".format(self.name))
    
    def connect_com_palyer(self):
        if self.player:
            for i in self.doc_commands.keys():
                self.player.doc_commands[i] = self.doc_commands[i]
            for i in self.commands.keys():
                self.player.commands[i] = self.commands[i]
    
    def desconnect_com_palyer(self):
        if self.player:
            for i in self.doc_commands.keys():
                del self.player.doc_commands[i]
            for i in self.commands.keys():
                del self.player.commands[i]
    
    def connect_player(self, player=None):
        if player:
            self.player = player
        if self.player:
            self.connect_com_palyer()
    
    def affiche_object(self):
        fiche = open(self.path, mode="r")
        for line in fiche.readlines():
            print(line)
        fiche.close()
    
    def description(self):
        self.affiche_object()
        print("name : {}".format(self.name))
        print("Description :",self.description_object)


class Weapon(Object):
    
    def __init__(self, name="", time=0, live=0, attack=0):
        Object.__init__(self, name, time, live)
        self.attack = attack
    

class Shield(Object):
    
    defense = 0


class Magic(Object):
    
    def __init__(self, palyer=None, name="", time=0, live=0):
        Object.__init__(self, name, time, live)
        self.palyer = palyer
        magic = 0
    
    def make_sor_enemie(self):
        pass
    
    def make_sor_myself(self):
        pass


class Instruction(Object):
    
    def __init__(self, player=None, name="", time=0, live=0, description_object="",path=""):
        Object.__init__(self, player=player, name=name, time=time, live=live, description_object=description_object, path=path)
        self.instruction = ""
        self.doc_commands = {
            "read_{}".format(self.name) : "Command to read instructions instructions of {} ".format(self.name),
        }
        
        self.commands = {
            "read_{}".format(self.name) : lambda : print(self.instruction),
        }
    
    def make_instruction(self, instruction=""):
        self.instruction = instruction
    
    

