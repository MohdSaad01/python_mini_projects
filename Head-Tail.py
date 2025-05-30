import random
a=random.randint(1,10)
b=input('"Head" or "Tail"').lower()

if a<=5:
	print("It's Heads")
	if b=="head":
		print("You Won")
	else:
		print("You lost")
else:
	print("It's Tails")
	if b=="tail":
		print("You won")
	else:
		print("You lost")