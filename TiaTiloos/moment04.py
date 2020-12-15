# Inlämmningsuppgift moment 04

import random as rnd


stop = 3 # int(input("How many loops do you wanna do?"))

while True:
    f = input("Vill du göra en ny beräkning? (ja/nej): ")
    
    # Mata in rektangelns two sidor

    k = 0
    
    kort = 5 #int(input("Korta sidan"))
  
    long = 4 #int(input("långa sidan"))

    while k == 0:
        höjd = int(input("Höjden: "))
    
        k += 1

        if isinstance(höjd, str):
            k = 0

        if höjd < 0:
            höjd = 1

        elif höjd > 10:
            höjd = 10
        

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

    if f == "nej":
        break

print (f)