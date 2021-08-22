import random

def roll(d):
    list = []

    for i in range(0,4):
        n = random.randint(1,d)
        list.append(n)

    list.sort(reverse=True)
    print(list)

    x = list[0] + list[1] + list[2]
    return(x)


print(roll(6))
