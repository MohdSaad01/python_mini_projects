import random
import string
password_list=[]

print("Welcome to a secure password generator program !")
num_letters = int(input("How many letters do you want in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_digits = int(input("How many numbers do you want in your password? "))

letters=list(string.ascii_letters)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers=list(string.digits)

for i in range(num_letters):
	password_list.append(random.choice(letters))
	
for p in range(num_symbols):
	password_list.append(random.choice(symbols))
	
for o in range(num_digits):
	password_list.append(random.choice(numbers))
	
random.shuffle(password_list)

password=''.join(password_list)


	
print(f"Your generated password is:{password}")