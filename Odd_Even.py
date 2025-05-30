try:
    number=int(input("Enter your desired number: "))
    if number%2==0:
        print(f"{number} is a even number")
    elif number%2!=0:
        print(f"{number} is a odd number")
except:
    print("Invalid Input")        