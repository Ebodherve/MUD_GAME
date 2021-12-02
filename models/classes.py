import os

#ironthread
#

class User:

    name = ""
    phone_num = ""
    email = ""
    password = ""
    
    def create_player(self):
        pass
    
    
class Character(User):
    
    name_perso = ""
    speed = 0
    stength = 0
    doc_commands = {
        "move" : "command to move at one specifique place",
        "destinations" : "commande to see all possibles destinations",
        "commands" : "Command to show commands documentation",
        "look" : "Command to describe your space",
        "info" : "Command to list informations of one object in your space",
        "take_object" : "Command to take one object in your space ",
        "inventory" : "Commands to list your objects",
        "clear_t" : "Command to clear terminale",
        "c_object" : "liste caracteristiques of one object",
        "attack" : "Command to attcak one enemie in your space",
    }
    
    def __init__(self, name="", space=None, description_perso="", live = 0, p_attack=0, history=None):
        self.name = name
        self.objects = {}
        self.space = space
        self.description_perso = description_perso
        self.p_attack = p_attack
        self.live = live
        self.know_story(history)
        self.commands = {
            "move" : lambda : self.move(),
            "destinations" : lambda : self.list_p_destinations(),
            "commands" : lambda : self.show_doc_commands(),
            "info" : lambda : self.info_space(),
            "look" : lambda : self.look_space(),
            "take_object" : lambda : self.take_object(),
            "inventory" : lambda : self.list_own_object(),
            "clear_t" : lambda : os.system("clear"),
            "c_object" : lambda : self.object_carac(),
            "attack" : lambda : self.attack(),
            }
        
    def attack(self):
        #Function to attack enemie
        en = input("type the enemie you want to attak : ")
        enemies = self.space.possess_enemi
        if en in enemies.keys():
            en1 = enemies[en]
            en1.live -= self.p_attack/2
            self.live -= en1.p_attack/2
            print("Your state")
            self.state()
            print("")
            en1.state()
            if en1.live<=0:
                print(" Your enemie is die ")
                del self.space.possess_enemi[en]
            elif self.live<=0:
                self.die()
        else:
            print(" This space not have this enemie ")
    
    def state(self):
        print("name : {}".format(self.name))
        print("live : {}".format(self.live))
        print("attack power : {}".format(self.p_attack))
    
    def die(self):
        print("You was killed, the party is finished")
        self.history.stop()
    
    def know_story(self, history):      
        self.history = history
        
    def info_space(self):
        #Function to list object in the space of player
        enemies = self.space.possess_enemi
        objects = self.space.objects_space
        charac = self.space.possess_charcater

        ob = input("Object that you want to describe : ")
        if ob in objects.keys():
            objects[ob].description()
        elif ob in enemies.keys():
            enemies[ob].description()
        elif ob in charac.keys():
            charac[ob].description()
        else:
            print("Not found ...")
    
    def move(self):
        #manage deplacements
        space = input("Enter your destinations : ")
        if space in self.destinations():
            new_space = self.space.possible_destinations[space]
            self.move_to_space(new_space)
            self.space.description_space()
        else :
            print("enter valide destination")
    
    def move_to_space(self, new_space):
        #function to move at one specific place
        if self.space == None:
            new_space.connect_player(self)
        else:
            self.space.deconnect_player(self, new_space)
    
    def destinations(self):
        #function that return all possible destinations
        if self.space :
            return self.space.possible_destinations.keys()
        return []
    
    def list_p_destinations(self):
        #function that list all destinations 
        for destination in self.destinations() :
            print(destination)
    
    def action(self, command):
        # function that manage the inter of commands
        try:
            print("")
            self.commands[command]()
            print("")
        except:
            print("")
            print("-------------------------------- Enter valid command --------------------------------")

    def show_doc_commands(self):
        # function that show the list of cmmands
        print("|----------------- The list of commands -----------------|")
        for i, j in self.doc_commands.items():
            print(i,":",j)

    def position(self):
        #The function who give the position of player
        if self.space:
            return self.space.name
        else :
            return "at non space"
        
    def look_space(self):
        if self.space:
            self.space.description()
    
    def list_objects_space(self):
        #function to list objects in the space
        if len(self.space.objects_space)>0:
            for obj in self.space.objects_space.keys():
                print(obj)
        else:
            print("This space not have objects")

    def take_object(self):
        #function to take one object in one space
        ob = input("Object that you want to take : ")
        if ob in self.space.objects_space.keys():
            self.objects[ob] = self.space.objects_space[ob]
            self.objects[ob].connect_player(self)
            #self.objects[ob].connect_player(self)
            del self.space.objects_space[ob]
            input("('Press entrer to continu')You have take this object : {} ".format(ob))
        else:
            print("The object that you specified is not in this space")
    
    def list_own_object(self):
        #Function to list objects of the player
        if len(self.objects)>=1:
            for ob in self.objects.keys():
                print(ob)
        else:
            print("You not have objects_________")
    
    def object_carac(self):
        #Function to list caracteristiques of objects on this space
        ob = input("Enter object that you want to list caracteristiques")
        if ob in self.objects.keys():
            self.objects[ob].list_caracteristiques()
        else :
            print("You not have this object")
    
    def description(self):
        print(self.name)
        print(self.description_perso)

class Map:
    
    name = ""
    story = "story"
    type_map = "type"
    space_first = None
    spaces = []

        

class Space :
    def __init__(self, name=None, description=""):
        self.objects_space = {}
        self.possess_enemi = {}
        self.possess_charcater = {}
        self.name = ""
        self.perso = None
        self.possible_destinations = {}
        self.description_text = description

        if name is not None :
            self.name = name

    def connect_player(self, perso):
        perso.space = self
        self.perso = perso
        
    def deconnect_player(self, perso, new_space):
        self.perso = None
        new_space.connect_player(perso)
    
    def connection_auther_space(self, liste_space = []):
        for space in liste_space:
            self.possible_destinations[space.name] = space
    
    def add_object(self, object_space = []):
        for ob in object_space :
            self.objects_space[ob.name] = ob
    
    def add_perso(self, perso):
        for e in perso:
            self.possess_charcater[e.name] = e

    def add_enemie(self, enemie):
        for e in enemie:
            self.possess_enemi[e.name] = e
    
    def description(self):
        print("This space is {} ".format(self.name))
        if len(self.objects_space)>0:
            print("Liste of objects : ")
            for i in self.objects_space.keys():
                self.objects_space[i].affiche_object()
                print(i)
        else:
            print("**** This space not have objects ****")

        print("")

        if len(self.possess_enemi)>0:
            print("List of enemmies")
            for i in self.possess_enemi.keys():
                print(i)
        else:
            print("**** This space not have enemies ****")

        print("")

        if len(self.possess_charcater)>0:
            print("List of character")
            for i in self.possess_charcater.keys():
                print(i)
        else:
            print("**** This space not have character ****")
        print("")
    
    def description_space(self):
        print(self.description_text)
    

class Enemie(Character):
    
    def __init__(self, name="", space=None, description_perso="", live = 0, p_attack=0, history=None, path=None):
        Character.__init__(self, name=name, space=space, description_perso=description_perso, live=live, p_attack=p_attack, history=history)
        self.path = path

    def description(self):
        Character.description(self)
        self.affiche()
        print("live : {} ".format(self.live))
        print("power attack : {} ".format(self.p_attack))
    
    def affiche(self):
        if self.path:
            fiche = open(self.path, mode="r")
            for line in fiche.readlines():
                print(line)
            fiche.close()

            
