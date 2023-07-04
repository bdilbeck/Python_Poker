import random
import itertools

deck=[
'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']

def suit(card):
     return card[-1] #Defines a card's suit
                     #https://www.youtube.com/watch?v=PZLCOgubhEE

display=['''┌─────────┐
│A        │
│         │
│    ♠    │
│         │
│        A│
└─────────┘''','''┌─────────┐
│2        │
│         │
│    ♠    │
│         │
│        2│
└─────────┘''','''┌─────────┐
│3        │
│         │
│    ♠    │
│         │
│        3│
└─────────┘''','''┌─────────┐
│4        │
│         │
│    ♠    │
│         │
│        4│
└─────────┘''','''┌─────────┐
│5        │
│         │
│    ♠    │
│         │
│        5│
└─────────┘''','''┌─────────┐
│6        │
│         │
│    ♠    │
│         │
│        6│
└─────────┘''','''┌─────────┐
│7        │
│         │
│    ♠    │
│         │
│        7│
└─────────┘''','''┌─────────┐
│8        │
│         │
│    ♠    │
│         │
│        8│
└─────────┘''','''┌─────────┐
│9        │
│         │
│    ♠    │
│         │
│        9│
└─────────┘''','''┌─────────┐
│10       │
│         │
│    ♠    │
│         │
│       10│
└─────────┘''','''┌─────────┐
│J        │
│         │
│    ♠    │
│         │
│        J│
└─────────┘''','''┌─────────┐
│Q        │
│         │
│    ♠    │
│         │
│        Q│
└─────────┘''','''┌─────────┐
│K        │
│         │
│    ♠    │
│         │
│        K│
└─────────┘''']
#Courtesy of ChatGPT

#for lines in zip(*map(str.splitlines, display)):
    #print(*(line.ljust(5) for line in lines))
#Borrowed from tobias_k on Stackoverflow


player_chips=10.00
cpu1_chips=10.00
community_pot=0.0


print("Welcome to Texas Hold'em!\n")



while True:
    playerIn=True
    cpu1In=True
    player_hand=[]
    cpu1_hand=[]
    community_cards=[]                                 #Resets everything in order to start a new round

    actual_player_hand=player_hand + community_cards 
    actual_cpu1_hand=cpu1_hand + community_cards       #Game logic


    def deal_card(turn):
        card=random.choice(deck)
        turn.append(card)
        deck.remove(card)

    for _ in range(2):
        deal_card(cpu1_hand)
        deal_card(player_hand)

    while playerIn: #or cpu1In
            print(f"Your hand:{player_hand}")
            print(f"Community Cards:{community_cards}")
            print(f"Your Chips: ${player_chips}\n")
            while True:
                try:
                    fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")
                except ValueError:
                        print("Invalid Input!")
                        continue
                if fold_or_bet=='1':
                        print("Player folds!")
                        playerIn=False
                        break
                elif fold_or_bet=='2':
                        try:
                            bet=float(input("Enter an amount to bet."))
                        except ValueError:
                                print("That is not an amount!")
                                continue
                        if bet>player_chips:
                            print("You don't have that many chips!")
                            continue
                        else:
                            print(bet)
                            player_chips-=bet
                            community_pot+=bet
                            break

            if playerIn and len(community_cards)==0:
                for _ in range(3):
                    deal_card(community_cards)

            print(f"Your hand:{player_hand}")
            print(f"Community Cards:{community_cards}")
            print(f"Your Chips: ${player_chips}\n")
            print(f"Community Pot: ${community_pot}")
            
            while True:
                try:
                    fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")
                except ValueError:
                        print("Invalid Input!")
                        continue
                if fold_or_bet=='1':
                        print("Player folds!")
                        playerIn=False
                        break
                elif fold_or_bet=='2':
                        try:
                            bet=float(input("Enter an amount to bet."))
                        except ValueError:
                                print("That is not an amount!")
                                continue
                        if bet>player_chips:
                            print("You don't have that many chips!")
                            continue
                        else:
                            print(bet)
                            player_chips-=bet
                            community_pot+=bet
                            break


            if playerIn and len(community_cards)==3:
                for _ in range(1):
                    deal_card(community_cards)

            print(f"Your hand:{player_hand}")
            print(f"Community Cards:{community_cards}")
            print(f"Community Pot:{community_pot}")

            #fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")

            while True:
                try:
                    fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")
                except ValueError:
                        print("Invalid Input!")
                        continue
                else:
                        if fold_or_bet=='1':
                            print("Player folds!")
                            playerIn=False
                            break
                        elif fold_or_bet=='2':
                            try:
                                bet=float(input("Enter an amount to bet."))
                            except ValueError:
                                print("You cannot bet that amount!")
                                continue
                            else:
                                if bet<=player_chips:
                                    print(bet)
                                    player_chips-=bet
                                    community_pot+=bet
                                    break
                    
            if playerIn and len(community_cards)==4:
                for _ in range(1):
                    deal_card(community_cards)

            print(f"Your hand:{player_hand}")
            print(f"Community Cards:{community_cards}")
            print(f"Community Pot:{community_pot}")


            #if playerIn and len(community_cards)==5:

            while True:
                        try:
                                fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")
                        except ValueError:
                                print("Invalid Input!")
                                continue
                        else:
                                if fold_or_bet=='1':
                                    print("Player folds!")
                                    playerIn=False
                                    break
                                elif fold_or_bet=='2':
                                    bet=float(input("Enter an amount to bet."))
                                    if bet<=player_chips:
                                        print(bet)
                                        player_chips-=bet
                                        community_pot+=bet
                                        break

            print("Let's see who has the best hand!")
            print(f"Your hand:{player_hand}")
            print(f"CPU hand:{cpu1_hand}")
            print(f"Community Cards:{community_cards}")
            print(f"${community_pot} goes to the winner!")

            player_chips+=community_pot       #Gives the money back to player. Once game is complete this will be changed to give the winner the money.

            print(f'Your Chips: {player_chips}')
            print(f'CPU Chips: {cpu1_chips}')
                                
            playerIn=False
            keepplaying=input("Play another round? Y/N ")
            if keepplaying == "Y":
                 pass
            elif keepplaying == "N":
                 print("See you later!")
            else:
                 print("Please enter Y or N to continue or quit.")
                
            

            

            






