def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

calc={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}    
    
operation=0   
print("""
 _____________________
|  _________________  |
| |    CALCULATOR   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
""")
loop_continue=True
a=int(input("What is the first number: "))

while loop_continue:
    action=input('''What type of calculation do you want to perform ? 
"+"
"-"
"*"
"/" 
''')
    b=int(input("What is the Second number: "))

    if action in calc:
        operation=calc[action]
        result=operation(a,b)
        print(result)   
    else:
        print("Invalid Input")        

    restart=input(f"Do you want to contiue with {result}? Type 'yes' or 'no'! ")
    if restart=="yes":
        a=result
    else:    
        print("Thanks for using the calculator")
        loop_continue=False