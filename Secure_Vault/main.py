from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2,4)
    num_digits = random.randint(2,4)

    letters = list(string.ascii_letters)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = list(string.digits)
    password_list=([random.choice(letters) for _ in range(num_letters)]+
                   [random.choice(symbols) for _ in range(num_symbols)]+
                   [random.choice(numbers) for _ in range(num_digits)])

    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_write.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_write.get()
    email=id_write.get()
    password=pass_write.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Error",message="Please fill all the details")
    else:
        ask=messagebox.askokcancel(title="Please confirm the details",message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        if ask:
            with open("data.txt","a") as data:
                    data.write(f"{website} | {email} | {password}\n")
                    website_write.delete(0, END)
                    pass_write.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

label_website=Label(text="Website:")
label_website.grid(row=1,column=0)
website_write=Entry(width=35)
website_write.focus()
website_write.grid(row=1,column=1,columnspan=2)

label_id=Label(text="Email/Username:")
label_id.grid(row=2,column=0)
id_write=Entry(width=35)
id_write.insert(0,"ansari.mohdsaad25@gmail.com")
id_write.grid(row=2,column=1,columnspan=2)

label_pass=Label(text="Password:")
label_pass.grid(row=3,column=0)
pass_write=Entry(width=25)
pass_write.grid(row=3,column=1)

genpass_button=Button(text="Generate Password",command=password_generator)
genpass_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()