import random
class pokemon():
    def __init__(self,name,element,health,speed):
        self.name=name.title()
        self.element=element
        self.current_health=health
        self.max_health=health
        self.speed=speed
        is_alive=True

    def light_attack(self,enemy):

        damage=random.randint(15,25)
        print(self.name+" performed "+self.moves[0])
        print("damage:"+str(damage))
        self.current_health -= damage

    def heavy_attack(self,enemy):
        damage=random.randint(0,50)
        print(self.name+" performed "+self.moves[1])
        if damage < 10:
            print("Attack is missed")
        else:
            print("damage:"+damage)
            self.current_health -= damage

    def restore(self):
        heal=random.randint(15,25)
        print(self.name + " performed " + self.moves[2])
        print("Healed:"+heal)
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        if self.current_health <= 0:
            print(self.name+" is fainted")
            is_alive=False
            print("press ENTER to continue")

    def show_status(self):
        print("Name:"+self.name +"\nElement:"+self.element+"\nCurrent health:"+self.current_health+
              "\nMaximum health:"+self.max_health+"\nSpeed:"+self.speed)