class player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.ord = ord

    def __str__(self):
        return 'name=' + self.name+ ' race= ' + self.race

char_list = []

while(True):

    name = input("what is your character's name?: ")
    race = input("What is your character's race?: ")

    char_list.append(player(name, race))

    option = int(input("press 0 if you want to add another character:"))

    if(option):
        break

for i in char_list:
    print('>', i)
