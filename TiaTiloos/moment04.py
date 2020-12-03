# Inlämmningsuppgift moment 04

import random as rnd


stop = 3 # int(input("How many loops do you wanna do?"))

#class

#def continue_or_nah():

f = input("Vill du göra en ny beräkning? (ja/nej)")

while f == "ja":

    # Mata in rektangelns two sidor

    kort = 5 #int(input("Korta sidan"))

    long = 4 #int(input("långa sidan"))


    # beräkna och skriv ut rektangelns area
    area=kort*long

    print(area)


    # om båda sidorna är lika långa ...
    if kort == long:
        print("Detta är en kvadrat")   # ... tala om att det är en kvadrat

    # Loopa höjden från 1 till 10
    for j in range(1,10):
        volume = j*area  # Beräkna volymen och skriv ut den
        print(f"Volymen {j} av rektangeln är {volume}")
    #else:
     #   print("Detta är en rektangel")

    

print (f)

