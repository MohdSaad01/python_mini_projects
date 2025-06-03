import random
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
print(r'''
🂡 🂱 🃁 🃑  🂠 BLACKJACK 🂠  🃑 🃁 🂱 🂡
''')
play=input("Do you want to play a game of blackjack? Type 'yes' or 'no': ")
player_cards=[]
player_score=0
if play=='yes':
    print("*************")
    player_cards=[random.choice(cards),random.choice(cards)]
    player_score=sum(player_cards)
    computer_1=(random.choice(cards))
    computer_2=(random.choice(cards))
    computer_score=computer_1+computer_2
    print(f" Your Cards {player_cards}, current score {player_score}")
    print(f"Computers first cards [{computer_1}]")
    while True:
        another=input("Type 'y' to get another card or 'n' to  pass: ")
        if another=="y":
            player_cards.append(random.choice(cards))
            player_score=sum(player_cards)
            while player_score>21 and 11 in player_cards:
                player_cards[player_cards.index(11)]=1
                player_score=sum(player_cards)
            print(f" Your Cards {player_cards}, current score: {player_score}")
            print(f"Computers first cards [{computer_1}]")
        else:
            print(f" Final Cards {player_cards}, Final score: {player_score}")
            if computer_score>17:
                print(f"Computer's Final cards [{computer_1,computer_2}] Final score: {computer_score}")
            elif computer_score<17:
                    computer_3=(random.choice(cards))
                    computer_score=computer_1+computer_2+computer_3
                    print(f"Computer's Final cards [{computer_1,computer_2,computer_3}] Final score: {computer_score}")
            if player_score>computer_score:
                print("You win 🥳")
                break
            elif player_score<computer_score:
                print("You lose 😞")
                break  
            else:
                print("It's a draw🤔")
                break         
                
        if player_score>21:
            print("You went over 21 you lose 😭")
            break
            
        if computer_score>21:
            print("The computer went over 21! You Win 😁")
            break    
elif play =="no":
    print("Game Over 😭")    

else:
    print("❌Invalid Input❌")    