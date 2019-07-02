import random
import math

class character:
    @staticmethod 
    def getenemyStats():
        return      {
                    'Armor_value':0,
                    'Evade_value':0,
                    }
    @staticmethod
    def getplayerStats():
        return      {
                    'Armor_value':0,
                    'Evade_value':0,
                    'Zombie_kill_chance':0,
                    'Coin_multiplier':1,
                    }
    @staticmethod
    def getplayerItems():
        return {
                'SuperTonic':0,
                'Armor_item':0,
                'Evade_item':0,
                'Power_item':0,
                'Zombie_exterminator':0,
                'Swap_item':0,
                'increase_coin_multiplier':0,
                }
    
    def __init__(self, health, power, Class, stats):
        self.health = health
        self.power = power
        self.Class = Class
        self.stats =  stats
    
    def evasion(self):
        evada = 1/4 * math.pow(self.stats['Evade_value'], 2) + 10
        if random.randint(0, 100) <= evada:
            evade = 0
        else:
            evade = 1
        return evade

    def damage(self, character):
        print(self.__dict__)
        print(character.stats)

        return character.evasion() * ((100 * self.power)/(character.stats['Armor_value'] + 100))
    
    def alive(self):
        return self.health > 0

    def dead(self):
        if self.health <= 0 and self.Class != 'Zombie':
            return

class hero(character):
    def __init__(self, health, power, Class, stats, coins, items):
        super().__init__(health, power, Class, stats)
        self.coins = coins
        self.items = items
        

    def attack(self, character):
        if self.Class == 'Warrior' and random.randint(0,4) == 0:
            print("Warrior landed a critical strike dealing twice the damage!!")
            character.health -= self.damage(character) * 2 
        else:
            character.health -= self.damage(character)
        

    
        
class enemy(character):
    def __init__(self, health, power, Class, stats, bounty):
        super().__init__(health, power, Class, stats)
        self.stats = stats
        self.bounty = bounty
    
    def attack(self, character):
        character.health -= self.damage(character)

char_dic = {
            "Goblins": 0,
            "Zombies": 0,
            }           
def numEnemies():
    return char_dic["Goblins"] + char_dic["Zombies"]

player_coins = 0
player_items = {
                'SuperTonic':0,
                'Armor_item':0,
                'Evade_item':0,
                'Power_item':0,
                'Zombie_exterminator':0,
                'Swap_item':0,
                'increase_coin_multiplier':0,
                }

player_specstats =  {
                    'Armor_value':0,
                    'Evade_value':0,
                    'Zombie_kill_chance':0,
                    'Coin_multiplier':1,
                    }

The_Shop = {
                'SuperTonic':10,
                'Armor_item':5,
                'Evade_item':5,
                'Power_item':10,
                'Zombie_exterminator':5,
                'Swap_item':5,
                'increase_coin_multiplier':20,           
}

Warrior = hero(10, 2, 'Warrior', character.getplayerStats(), 0, character.getplayerItems)
Medic = hero(10, 2, 'Medic', character.getplayerStats(), 0, character.getplayerItems)
Shadow = hero(1 , 2,'Shadow', character.getplayerStats(), 0, character.getplayerItems)
Shadow.stats['Evade_value'] = 10
def spawnGoblin():
    return enemy(4,2,'Goblin', character.getenemyStats(), 10)

goblins = 0
def goblin(number):
    char_dic['Goblins'] += number
    return char_dic['Goblins']
def goblin_dead():
    char_dic['Goblins'] -= 1
    return char_dic['Goblins']

def goblins_remaining():
    return char_dic['Goblins']
def goblin_next(Hero):
    player_tempcoins = 0
    while numEnemies() > 0 and Hero.alive():
        Goblin = spawnGoblin() 
        while Goblin.alive() and Hero.alive():
            print('A Goblin is present.')
            attackinput = input('''
            1. to attack
            ''')
            if attackinput == '1':
                Hero.attack(Goblin)
                print("You dealt " + str(Hero.power)  + " damage")
            else:
                print("Invalid Input")
            if Goblin.alive() == False:
                print("The Goblin is dead! you found 5 coins")
                player_tempcoins += 5
                goblin_dead()
                print("There is " + str(goblins_remaining()) + " " )
            else:
                Goblin.attack(Hero)
                print("The Goblin lives and deals " + str(Goblin.power) + " damage")
                print("You have " + str(Hero.health) + " health")
        if Hero.alive() == False:
            break
    if Hero.alive() == False:
        print("You died")
    else:
        print("Level Completed! \nYour bank gained " + str(player_tempcoins)+ " coins!")
    return player_tempcoins
    
            
def fighter1(enemies, Hero):
    while numEnemies() >0 and Hero.alive():
        playerinput1 = input("There are " + str(enemies) + " enemies would you like to fight them"'''
        1. Lets get them!
        2. go to Shop
        3. Maybe I should give up...''')
        menu = True
        while menu and numEnemies() > 0:
            if playerinput1 == '1':
                goblin_next(Hero)
            if Hero.alive() == False:
                menu = False
            

def shop():
    print('Welcome to the Shop!')


    
def heroSelection():
    heroinput = input("Choose a Hero\n"'''
        1. Warior 'A fierce beast'
        2. Medic  'Has regenetive abilities'
        3. Shadow 'A Mysterious creature things cant seem to hit this beast'
        ''')
    herosel = True
    while herosel:
        if heroinput == '1':
            print("Warrior selected")
            Hero = Warrior
            herosel = False
        elif heroinput == '2':
            print("Medic selected")
            Hero = Medic
            herosel = False
        elif heroinput == '3':
            print("Shadow selected")
            Hero = Shadow
            herosel = False
        else:
            print("Invalid Input")
    return Hero
        
def Menus():
    Startinput = input('''
    Menu
    1. Start Game
    2. 
    3. Exit Game

    ''')
    menu1 = True
    while menu1 == True:
        if Startinput == '1':
            menu1 = False
            print('Good luck!')
            break
        elif Startinput == '2':
            break
        else:
            print('Invalid Input')
        


game = True
Hero = heroSelection()
Menus()

while game:
    print("Welcome to Code Defenders!!!")
    
    
    
    
    
    goblin(2)
    print(char_dic)
    fighter1(numEnemies(), Hero)

    print(Hero.health)
    if Hero.alive() == False:
        break


        
    
