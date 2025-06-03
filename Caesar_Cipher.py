alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
print(r''',adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88                                                                       
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')
def caesar():
    if direction=="encode":
        def encrypt(original_text,shift_amount):
            cipher_text=""
            for i in original_text:
                if i in alphabet:
                    position=alphabet.index(i)
                    new_position=(position+shift_amount)%26
                    cipher_text+=alphabet[new_position]
                else:
                    cipher_text+=i    
            print(f"Your encoded text is:{cipher_text}")        
        encrypt(text,shift)

    elif direction=="decode":
        def decrypt(original_text,shift_amount):
            decrypt_text=""
            for i in original_text:
                if i in alphabet:
                    position=alphabet.index(i)
                    new_position=(position-shift_amount)%26
                    decrypt_text+=alphabet[new_position]
                else:
                    decrypt_text+=i    
            print(f"Your decoded text is:{decrypt_text}")        
        decrypt(text,shift) 
    
    else:
        print("You entered wrong input")    
        
again=True        
while again:
    direction=input("Type 'encode' to encrypt and 'decode'to decrypt: ").lower()
    text=input("Type your message: ").lower()
    shift=int(input("Type to shift number: "))
    caesar()
    again=input("If you want to run the program again type 'yes' or 'no' if you don\'t want to: ").lower()
    
    if again=="no":
        print("GoodBye!")
        again=False
        