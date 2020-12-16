import kortlek


# behöver räkna ut värden
def countPoints(hand):
    points = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            points += 10
        elif kort == "A" and points < 11:
            points += 11
        elif kort == "A" and points >= 11:
            points += 1
        else:
            points += kort
    return points



# Ha kåll på handen
def skrivUtHanden(hand):
    print("Your cards are: ", end="")
    for kort in hand:
       print(str(kort) + ", ", end="")

# Vem vinner
def checkWinner(hand, dealer):
    dealerPoints = countPoints(dealer)
    playerPoints = countPoints(hand)

    print(f"Dealers cards are {dealer[0]} och {dealer[1]}")
    print(f"Dealers total points are {dealerPoints}")
    print(f"Your tota; points are {playerPoints}")

    if playerPoints == 21:
        print("Blackjack! You win!")
    elif playerPoints <= dealerPoints or playerPoints > 21:
        print("Dealern wins and takes your money")
    else:
        print("You WIN!")

# spel-loop
while True:
    spela = input("Do you wish to play blackjack? (y for yes, another key for no) : ")

    if spela != "y":
        break    # Hoppar ut från while satsen

    lek = kortlek.skapaKortlek()
    #print(lek)

    # dealer tar två kort
    dealer = [lek.pop(0), lek.pop(0)]
    print(f"Dealer's first card is {dealer[0]}")

    hand = [lek.pop(0), lek.pop(0)]
    print(f"Your first two cards are: {hand[0]} and {hand[1]}")
    
    cont = True

    # göra val (Ta ett till kort eller stanna)
    while cont:
        #ask the user if they want to take a new card
        taKort = input("Take new card? (y for Yes, other key for No) : ")
        if taKort == "y":
            #dela ut kort
            hand.append(lek.pop(0))
            #skriv ut hand
            skrivUtHanden(hand)
        else:
            cont = False

    checkWinner(hand, dealer)

print("End of game")