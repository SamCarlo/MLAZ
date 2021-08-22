class Player:
    def __init__(self, name, race):
        print('Inside Player constructor')
        self.name = name
        self.race = race

    def __str__(self):
        print('Inside Player Print Representation')
        return 'name=' + self.name+ ' race= ' + self.race

    def cast_spell(self, name):
        print('prepare to cast...', self, name)
        return 'casting' + name + '!'

player_list = []

while(True):

    name = input("what is your character's name?: ")
    race = input("What is your character's race?: ")
    player = Player(name, race)
    player_list.append(player)

    print(player.cast_spell('fireball'))
    option = int(input("press 0 if you want to add another character:"))

    if(option):
        break

for player in player_list:
    print('>', player)
