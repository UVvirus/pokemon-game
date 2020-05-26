from pokemon import pokemon
import random
from fire import fire
from grass import grass
from water import water


class game(pokemon):
    def __init__(self):
        #super().__init__(name, element, health, speed)
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
            pokemon=fire(name,element,health,speed)
        elif element == "WATER":
            pokemon = water(name,element,health,speed)
        else:
            pokemon = grass(name,element,health,speed)


    def choose_pokemon(self):
        starters=[]
        while len(starters) < 3:
            pokemon=self.create_pokemon()
            valid_pokemon = True

            for starter in starters:
                if starter.name == pokemon.name or starter.element == pokemon.element:
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
        print("\nWhat would you like to do...")
        print("(1) - " + pokemon.moves[0])
        print("(2) - " + pokemon.moves[1])
        print("(3) - " + pokemon.moves[2])
        print("(4) - " + pokemon.moves[3])
        choice=int(input("Enter a choice:"))
        print()
        print("-----------------------------------------------------------------")
        return choice
    def player_attack(self,move,player,computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore(computer)
        elif move == 4:
            player.special_attack(computer)
        computer.faint()

    def computer_attack(self,player,computer):
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore(player)
        elif move == 4:
            computer.special_attack(player)
        player.faint()

    def battle(self,player,computer):
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move,player,computer)
            if computer.is_alive:
                self.computer_attack(player,computer)
        else:
            self.computer_attack(player,computer)
            if player.is_alive:
                self.player_attack(move,player,computer)

print("Welcome to Pokemon!")
print("Can you become the worlds greatest Pokemon Trainer???")
print("\nDon't worry! Prof Eramo is here to help you on your quest.")
print("He would like to gift you your first Pokemon!")
print("Here are three potential Pokemon partners.")
input("Press Enter to choose your Pokemon!")

playing_main=True

while playing_main:
    Game=game()
    player= Game.choose_pokemon()
    print("\nCongratulations Trainer, you have chosen " + player.name + "!")
    input("\nYour journey with " + player.name + " begins now...Press Enter!")
    # While your pokemon is alive, continue to do battle
    while player.is_alive:
        computer= Game.create_pokemon()
        print("\nOH NO! A wild " + computer.name + " has approached!")
        computer.show_stats()
        while computer.is_alive and player.is_alive:
            Game.battle(player,computer)
            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()
    print("---------------------------------------------------------------------------")
    if player.is_alive:
        Game.battles_won += 1
        print("\nPoor " + player.name + " has fainted...")
        print("But not before defeating " + str(game.battles_won) + " Pokemon!")
        choice = input("Would you like to play again (y/n): ").lower()
        if choice != 'y':
            playing_main = False
        print("Thank you for playing Pokemon!")
