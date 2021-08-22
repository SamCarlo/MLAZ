import random

#Gives the instance an attribute for stamina
def roll(d):
    print("inside dice roller")
    list = []

    for i in range(0,4):
        n = random.randint(1,d)
        list.append(n)

    list.sort(reverse=True)
    #print('your die values = ' + str(list))

    stam = list[0] + list[1] + list[2]
    return stam

class Player:
    #Takes a variable with a given name
    def __init__(self, name):
        self.name = name
        self.stam = roll(6)
        self.strength = roll (6)
        self.wisdom = roll (6)

    def __str__(self):
        return('Hero`s name: ' + str(self.name) +
        ' ' + 'Stamina: ' + str(self.stam) +
        ' ' + 'Strength: ' + str(self.strength) +
        ' ' + 'Wisdom: ' + str(self.wisdom))


hero_list = []

while(True):
    name = input("what is your hero's name?")

    #creates an instance with a name and a stam
    hero = Player(name)
    hero_list.append(hero)

    option = int(input('Press 0 to add another hero.'))
    if(option):
        break

print('Total # of heros in this party: ' + str(len(hero_list)))

#Why doesn't this print out multiple heros?
for hero in hero_list:
    print(hero)
    print('----------------------')


#player_list = []

#while(True):
    #Gather the name, race, and school of the player's DND character
    #name = input("what is your character's name?")
    #race = input("what is your character's race?")
    #school = input("what is your character's class?")
#
    #Roll the character's attributes
