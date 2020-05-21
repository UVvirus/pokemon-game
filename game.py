import pokemon
import random

from fire import fire
from grass import grass
from water import water


class game(pokemon):
    def __init__(self):
        self.pokemon_elements=["FIRE","WATER","GRASS"]
        self.pokemon_names=['Chewdie', 'Spatol',
'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot',
'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        self.battles_won=0

    def create_pokemon(self):
        health=random.randint(70,100)
        speed=random.randint(1,10)
        element=self.pokemon_elements[random.randint(0,len(self.pokemon_elements)-1)]
        name=self.pokemon_names[random.randint(0,len(self.pokemon_names)-1)]

        if element =="FIRE":
            pokemon=fire(self,name,element,health,speed)
        elif element == "WATER":
            pokemon = water(self,name,element,health,speed)
        else:
            pokemon = grass(name,element,health,speed)


    def choose_pokemon(self):
        starters=[]
        while len(starters) < 3:
            pokemon=self.create_pokemon()
            valid_pokemon = True
            for starter in starters:
                if starter.name == pokemon.name or starter.element ==pokemon.element:
                    valid_pokemon = False
            if valid_pokemon:
                starters.append(pokemon)
        for starter in starters:
            starter.show_stats()
            starter.move_info()

        print("choose one pokemon\n1)"+starters[0].name)
        print("2)"+starters[1].name+"\n3)"+starters[2].name)
        choice=int(input("choose any one:"))
        pokemon=starters[choice - 1]
        return pokemon

    def get_attack(self,pokemon):
