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
                'SuperTonic':5,
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
        return character.evasion() * ((100 * self.power)/(character.stats['Armor_value'] + 100))
    
    def alive(self):
        return self.health > 0

    def dead(self):
        if self.health <= 0 and self.Class != 'Zombie':
            return

class hero(character):
    def __init__(self, health, power, Class, stats, coins, items, level):
        super().__init__(health, power, Class, stats)
        self.coins = coins
        self.items = items
        self.level = level
        

    def attack(self, character):
        if self.Class == 'Warrior' and random.randint(0,4) == 0:
            damage = self.damage(character) * 2 
            if damage == 0:
                print("The " + character.Class + " has evaded " + self.Class + " attack!")
            else:
                print("Warrior landed a critical strike dealing " + str(damage) + " damage!!")
                character.health -= damage
        else:
            damage = self.damage(character)
            if damage == 0:
                print("The " + character.Class + " has evaded " + self.Class + " attack!")
            else:
                character.health -= damage
                print(self.Class + " did " + str(damage) + " to " + character.Class + "!")
        
def ask(question,input):
    userInput = input(question)
    valid = False
    while valid == False:
        if userInput not in input:
            print("Invalid input")
        else:
            valid = True
    
       
    
        
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

The_Shop = {
                'SuperTonic':10,
                'Armor_item':5,
                'Evade_item':5,
                'Power_item':10,
                'Zombie_exterminator':5,
                'Swap_item':5,
                'increase_coin_multiplier':20,           
}
def useItem(Hero):
    print(Hero.items)
    Item_List = []
    index = 0
    print('You have:')
    for item, value in Hero.items():
        if value > 0:
            print(str(index) + '. '+ item + ' : ' + str(value))
            Item_List.append(item)
            index += 1
    userinput1 = input('''
                        Inventory
                        1. Use Item
                        2. Exit
                        ''')
    if userinput1 == '1':   
        userInput = int(input('Select item: (0 - '+ str(index-1) + ')'))
        if Item_List[userInput] == 'SuperTonic':
            print("You've brought a SuperTonic ")
            Hero.health += 10
        elif Item_List[userInput] == 'Armor_item':
            print("You've brought a Armor_item ")
            Hero.stats['Armor_Value'] += 10
        elif Item_List[userInput] == 'Evade_item':
            print("You've brought a Evade_item")        
            Hero.stats['Evade_Value'] += 10
        elif Item_List[userInput] == 'Zombie_Exterminator':
            print("You've brought a Zombie_Exterminator ")
            Hero.stats['Zombie_Exterminator'] += 10
        elif Item_List[userInput] == 'Swap_item':
            print("You've brought a  Swap_item")
            Hero.health += 10
        elif Item_List[userInput] == 'increase_coin_multiplier':
            print("You've brought a increase_coin_multiplier")
            Hero.stats['increase_coin_multiplier'] += 2
        Hero.items[Item_List[userInput]] -= 1
        else:
            return
    


Warrior = hero(10, 2, 'Warrior', character.getplayerStats(), 0, character.getplayerItems(), 1)
Medic = hero(10, 2, 'Medic', character.getplayerStats(), 0, character.getplayerItems(), 1)
Shadow = hero(1 , 2,'Shadow', character.getplayerStats(), 0, character.getplayerItems(), 1)
Shadow.stats['Evade_value'] = 10
print((Warrior.__dict__))
def spawnGoblin():
    return enemy(4,2,'Goblin', character.getenemyStats(), 10)


def goblin(number):
    char_dic['Goblins'] += number
    return char_dic['Goblins']
def zombie(number):
    char_dic['Zombies'] += number
    return char_dic['Zombies']

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
            print("You have " + str(Hero.health) + " health")
            attackinput = input('''
            1. To attack
            2. To use an item
            3. To run
            ''')
            if attackinput == '1':
                Hero.attack(Goblin)
            elif attackinput  == '2':
                useItem(Hero)
            elif attackinput == '3':
                break
            else:
                print("Invalid Input")
            
            if Goblin.alive() == False and attackinput != '3':
                print("\nThe Goblin is dead! you found 5 coins")
                player_tempcoins += 5
                goblin_dead()
                print("There is " + str(goblins_remaining()) + "goblins remaining\n" )
            if Goblin.alive() == True and attackinput != '3':
                Goblin.attack(Hero)
                print("The Goblin lives and deals " + str(Goblin.power) + " damage\n")
                print("You have " + str(Hero.health) + " health\n")
        if Hero.alive() == False:
            break
    if Hero.alive() == False:
        print("You died")
    if Hero.alive() == True and attackinput != '3':
        print("Level " + str(Hero.level) + " Complete! \nYour bank gained " + str(player_tempcoins)+ " coins!\n")
        Hero.level += 1
    return player_tempcoins
    
def getInv(Hero):
    print(Hero.items)
    playerinput = input("Enter any key when done")
    if playerinput == 'asf':
        return
    else:
        return
            
def fighter1(enemies, Hero):
    menu = True
    while numEnemies() > 0 and Hero.alive() and menu:
        playerinput1 = input("\nThere are " + str(enemies) + " enemies would you like to fight them?\n"'''
        1. Lets get them!
        2. go to Shop
        3. Maybe I should give up...
        ''')
        
        
        if playerinput1 == '1':
            Hero.coins += goblin_next(Hero)
        elif playerinput1 == '2':
            shop(Hero)
        elif playerinput1 == '3':
            menu = False
        else:
            print("Invalid Input")
        if Hero.alive() == False:
            menu = False
    if playerinput1 == '3':
        return
            

def shop(Hero):
    shop = True
    while shop:
        Selection = False
        while Selection == False:
            print('Welcome to the Shop!')
            print('You have '+ str(Hero.coins) + 'coins.')
            item = ''
            itemInput = input('''
                            Items Available:
                            1. Supertonic 'Increase Health'
                            2. Armor Upgrade 
                            3. Evade Upgrade
                            4. Power Upgrade
                            5. Zombie_Exterminator 'Gives you a chance to kill a zombie'
                            6. Swap stats
                            7. Double coins
                            0. Exit shop
                            I. To look in inventory
                            ''')
            if itemInput == '1' and Hero.coins >= The_Shop["SuperTonic"]:
                item = 'SuperTonic'
                Selection = True
            elif itemInput == '2' and Hero.coins >= The_Shop["Armor_item"]:
                item =  'Armor_item'
                Selection = True            
            elif itemInput == '3' and Hero.coins >= The_Shop["Evade_item"]:
                item =  'Evade_item'
                Selection = True
            elif itemInput == '4' and Hero.coins >= The_Shop["Power_item"]:
                item =  'Power_item'
                Selection = True
            elif itemInput == '5' and Hero.coins >= The_Shop["Zombie_Exterminator"]:
                item =  'Zombie_Exterminator'
                Selection = True
            elif itemInput == '6' and Hero.coins >= The_Shop["Swap_item"]:
                item =  'Swap_item'
                Selection = True
            elif itemInput == '7' and Hero.coins >= The_Shop["increase_coin_multiplier"]:
                item =  'increase_coin_multiplier'
                Selection = True
            elif itemInput == '0':
                Selection = True
                break
            elif itemInput.lower() == 'i':
                getInv(Hero)
                print(Hero.items)
                
            else :
                print("Invalid Input")
            Hero.coins -= The_Shop[item]
        if itemInput == '0':
            break
        howManyInput = input('How many ' + item + "s would you like to buy?")
        quantity = int(howManyInput)
        if The_Shop[item] * quantity >= Hero.coins :
            Hero.coins -= The_Shop[item] * quantity
        else:
            print("Insufficient funds")
    anotherPurchaseInput = input('''
                                Would you like to make another purchase?
                                Y / N ?
                                ''')
    if anotherPurchaseInput.lower() == 'y':
        shop = True
    else:
        shop = False

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
    menu1 = True
    while menu1 == True:
        Startinput = input('''
        Menu
        1. Start Game
        2. Go to Shop
        0. Exit Game

        ''')
        
    
        if Startinput == '1':
            menu1 = False
            print('Good luck!')
            return True
        elif Startinput == '2':
            shop(Hero)
        elif Startinput == '0':
            return False
        else:
            print('Invalid Input')
        



Hero = heroSelection()

game = Menus()
while game:
    if Hero.level == 1:
        print("Welcome to Code Defenders!!!")
    else:
        print("Level "+ str(Hero.level))
    
    
    
    number_Goblins = Hero.level * 2
    goblin(number_Goblins)

    number_Zombies =  Hero.level - 4 
    
    if number_Zombies > 0:
        zombie(number_Zombies)
    
        
    
    print(char_dic)
    fighter1(numEnemies(), Hero)

    print(Hero.health)
    if Hero.alive() == False:
        break


        
    
