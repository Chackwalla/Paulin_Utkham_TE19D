import kortlek


# behöver räkna ut värden


# Ha kåll på handen
def skrivUtHanden(hand):
    print("Your cards are: ", end="")
    for kort in hand:
       print(str(kort) + ", ", end="")

# Vem vinner

# spel-loop
while True:
    spela = input("Do you wish to play blackjack? (y for yes, another key for no)")

    if spela != "y":
        break

    lek = kortlek.skapaKortlek()
    print(lek)

    # dealer tar två kort
    dealer = [lek.pop(0), lek.pop(0)]
    print(f"Dealer's first card is {dealer[0]}")

    hand = [lek.pop(0), lek.pop(0)]
    print(f"Your first two cards are: {hand[0]} and {hand[0]}")
    
    continue = True

    # göra val (Ta ett till kort eller stanna)
    while continue:
        #ask the user if they want to take a new card
        taKort = input("Take new card? (y for Yes, other key for No)")
        if taKort == "y"
            #dela ut kort
            hand.append(lek.pop(0))
            #skriv ut hand
            skrivUtHand(hand)
        else:
            continue = False
