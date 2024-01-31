from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    E3.delete(0, END)

    password_list = []
    l=[random.choice(letters) for num in range(random.randint(8, 10))]
    n=[random.choice(numbers) for num in range(random.randint(2,4))]
    s=[random.choice(symbols) for num in range(random.randint(2,4))]
    password_list=l+n+s
    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    E3.insert(END,password)
#FIND PASSWORD
def find_password():
    site=E1.get()
    try:
        with open("password_manager.json","r") as f:
            all_data = json.load(f)
            email = all_data[site]["email"]
            password = all_data[site]["password"]

    except FileNotFoundError:
        messagebox.showwarning("warning","No data file found")

    except KeyError:
        messagebox.showwarning("warning","No record found")
    else:
        messagebox.showinfo(site, f"email: {email}\npassword: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = E1.get()
    email = E2.get()
    password = E3.get()
    data={
        website:{
            "email":email,
            "password":password
        }
    }
    try:
        with open("password_manager.json", "r") as file:
            udata=json.load(file)
            udata.update(data)
    except FileNotFoundError:
        with open("password_manager.json", "w") as file:
            json.dump(data,file,indent=4)
    else:
        with open("password_manager.json", "w") as file:
            json.dump(udata,file,indent=4)
    E1.delete(0, END)
    E3.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manger")
window.config(padx=20,pady=20)
canvas=Canvas(height=200,width=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)
E1=Entry(width=17)
E1.grid(row=1,column=1,columnspan=1)
E1.focus()
E2=Entry(width=35)
E2.grid(row=2,column=1,columnspan=2)
E2.insert(END,"abhishekrana25112002@gmail.com")
E3=Entry(width=17)
E3.grid(row=3,column=1)
sb=Button(text="Search",command=find_password)
sb.grid(row=1,column=2)
gp=Button(text="Generate Password",command=generate_password)
gp.grid(row=3,column=2)
add=Button(text="Add",width=30,command=add_to_file)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()