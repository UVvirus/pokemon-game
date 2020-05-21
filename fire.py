from pokemon import pokemon
import random

class fire(pokemon):
    def __init__(self,name,element,health,speed):
        super().__init__(self,name,element,health,speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self,enenmy):
        print(self.name+" used "+self.moves[3])
        if enenmy.element == "GRASS":
            print("Its super effective")
            damage=random.randint(35,50)
        elif enenmy.element =="WATER":
            print("Not very effective")
            damage=random.randint(5,10)
        else:
            damage=random.randint(10,30)
            print("damage:"+damage)
            damage -= self.current_health

    def move_info(self):
        print("The pokemon moves are:")
        print(self.moves[0]+"\n lite attack\n")
        print(self.moves[1]+"\n heavy attack\n")
        print(self.moves[2]+"\nrestore\n")
        print(self.moves[3]+"\nspecial attack")