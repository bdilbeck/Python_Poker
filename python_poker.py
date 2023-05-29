import random
import itertools

deck=[
'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']


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

for lines in zip(*map(str.splitlines, display)):
    print(*(line.ljust(5) for line in lines))
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
    community_cards=[]
    actual_player_hand=player_hand + community_cards
    actual_cpu1_hand=cpu1_hand + community_cards


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
            while playerIn:
                fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")

                if fold_or_bet=='1':
                    print("Player folds!")
                    playerIn=False
                elif fold_or_bet=='2':
                    bet=float(input("Enter an amount to bet."))
                    if bet<=player_chips:
                        print(bet)
                        player_chips-=bet
                        community_pot+=bet
                    else:
                        print("Invalid Input!")

                else:
                    print("Invalid Input!")

                print(f"Your Chips: ${player_chips}")
                print(f"Community Pot: ${community_pot}")

                if playerIn and len(community_cards)==0:
                    for _ in range(3):
                        deal_card(community_cards)
                    
                print(f"Your hand:{player_hand}")
                print(f"Community Cards:{community_cards}")

                fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")

                if fold_or_bet=='1':
                    print("Player folds!")
                    playerIn=False
                elif fold_or_bet=='2':
                    bet=float(input("Enter an amount to bet."))
                    if bet<=player_chips:
                        print(bet)
                        player_chips-=bet
                        community_pot+=bet
                    else:
                        print("Invalid Input!")

                else:
                    print("Invalid Input!")
                
                if playerIn and len(community_cards)==3:
                    for _ in range(1):
                        deal_card(community_cards)

                print(f"Your hand:{player_hand}")
                print(f"Community Cards:{community_cards}")
                print(f"Community Pot:{community_pot}")

                fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")

                if fold_or_bet=='1':
                    print("Player folds!")
                    playerIn=False
                elif fold_or_bet=='2':
                    bet=float(input("Enter an amount to bet."))
                    if bet<=player_chips:
                        print(bet)
                        player_chips-=bet
                        community_pot+=bet
                    else:
                        print("Invalid Input!")

                else:
                    print("Invalid Input!")
                
                if playerIn and len(community_cards)==4:
                    for _ in range(1):
                        deal_card(community_cards)

                print(f"Your hand:{player_hand}")
                print(f"Community Cards:{community_cards}")
                print(f"Community Pot:{community_pot}")


                if playerIn and len(community_cards)==5:

                    fold_or_bet=input("Enter 1 to fold, or enter 2 to bet.")

                    if fold_or_bet=='1':
                        print("Player folds!")
                        playerIn=False
                    elif fold_or_bet=='2':
                        bet=float(input("Enter an amount to bet."))
                        if bet<=player_chips:
                            print(bet)
                            player_chips-=bet
                            community_pot+=bet
                        else:
                            print("Invalid Input!")

                    else:
                        print("Invalid Input!")

                    print("Let's see who has the best hand!")
                    print(f"Your hand:{player_hand}")
                    print(f"CPU hand:{cpu1_hand}")
                    print(f"Community Cards:{community_cards}")
                    
                    playerIn=False

           

        






