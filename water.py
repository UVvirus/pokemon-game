import pokemon
import random
class water(pokemon):
    def __init__(self,name,element,health,speed):
        super().__init__(self,name,element,health,speed)
        self.moves=['Bite', 'Splash', 'Dive', 'Water Cannon']

    def special_attack(self,enemy):
        print(self.name+" used "+self.moves[3])
        if enemy.element =="FIRE":
            print("massive damage")
            damage=random.randint(35,50)
        elif enemy.element == "GRASS":
            print("Not veryeffective")
            damage=random.randint(5,10)
        else:
            damage=random.randint(10,20)
            print("damage:"+damage)
            damage -= self.current_health

    def move_info(self):
        print(self.moves[0]+"\n lite attack")
        print(self.moves[1] + "\n heavy attack\n")
        print(self.moves[2] + "\nrestore\n")
        print(self.moves[3] + "\nspecial attack")