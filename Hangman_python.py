import random
word = [
    "apple",
    "banana",
    "cherry",
    "dragon",
    "elephant",
    "football",
    "giraffe",
    "hamburger",
    "internet",
    "jellyfish"
]
chosen_word=random.choice(word)
blank=""
length=len(chosen_word)
blank=length*"_ "
print('''
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

             _______
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / \ ''')
hangman_stages = [
    '''
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      /
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |___
    ''',  
    '''
     _______
    |/      |
    |
    |
    |
    |
    |
    |___
    '''   ]

lives=6
correct_letter=[]
game_over=False

while not game_over:
	print(f"******************** {lives}/6 lives left ********************")
	
	guess=input("Enter a letter: ").lower()
	display=""
	if guess in correct_letter:
				print(f"You already guessed the letter '{guess}'")
				continue
	if guess not in chosen_word:
				print("You guessed a wrong letter. You lose a life")
				lives-=1
	if lives==0:
		print(f"The Word was '{chosen_word}'. ******************** You Lose ********************")
		break
		
	for i in chosen_word:
			if i ==guess:
				display+=i
				correct_letter.append(guess)
			
				
			elif i in correct_letter:
				display+=i
			
			else:
				display+="_"
	print(display)
	

	if "_" not in display:
		print("You guessed all the letters.******************** You won ********************")
		game_over=True	
	print(hangman_stages[lives])