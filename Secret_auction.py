print("Logo")
more=True
bidders={}
while more:
    name=input("What is your name? ")
    bid=int(input("What is your maximum bid? $"))
    bidders[name]=bid        
    contestant=input("Are there any more players? Type 'yes'  or 'no'! ").lower()
    if contestant=="yes":
        print("\n"*100)
    else:
        more=False
        


highest_bid=0
winner_name=""
for i in bidders:
    current_bid=bidders[i]
    if current_bid>highest_bid:
        highest_bid=current_bid
        winner_name=i
        
print(f"The Winner of the auction is {winner_name}") 