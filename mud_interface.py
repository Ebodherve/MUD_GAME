from models import classes
from histories import h2

perso = classes.Character(name="my_self", space=classes.Space("depart"), live=20, p_attack=5)

story1 = h2.Search_Mother(perso)
print("***********- Start of game -***********")
story1.start()

