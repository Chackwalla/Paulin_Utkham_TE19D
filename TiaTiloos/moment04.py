# Inlämmningsuppgift moment 04

import random as rnd

stop = 7 # int(input("How many loops do you wanna do?"))

for i in range(1,stop):

    # Mata in rektangelns two sidor

    kort = 5 # int(input("Korta sidan"))

    long = 4 # int(input("långa sidan"))


    # beräkna och skriv ut rektangelns area

    print(kort*long)


    # om båda sidorna är lika långa
    if kort == long:
        print("Detta är en kvadrat")

    else:
        print("Detta är en rektangel")

print (i)