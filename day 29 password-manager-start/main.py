from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    site_name = name_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        site_name : {
            "email": email,
            "password": pw,
        }
    }


    if len(site_name) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="please do not leave blanks")
    else:
        is_ok = messagebox.askokcancel(title="Verify info", message="Please verify info")
        if is_ok:
            try:
                with open("detailsfile.json","r") as file:
                    #reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("detailsfile.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # update old data
                data.update(new_data)
                with open("detailsfile.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                name_entry.delete(0, END)
                name_entry.focus()
                pw_entry.delete(0, END)

def search_key():
    key_name = name_entry.get()
    with open("detailsfile.json", "r") as file:
        # reading old data
        data = json.load(file)
        if key_name in data:
            emailadd = data[key_name]["email"]
            passwords=data[key_name]["password"]
            print(emailadd, passwords)
        else:
            print("no")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

site_name = Label(text="Site Name :")
site_name.grid(column=0, row=1)
email_uname = Label(text="Email/Username :")
email_uname.grid(column=0, row=2)
password = Label(text="Password :")
password.grid(column=0, row=3)

name_entry = Entry(width=21)
name_entry.grid(column=1, row=1)
name_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "walukaweb@yahoo.com")
pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", command=generate_password, width=20)
gen_button.grid(column=2, row=3)
add_button = Button(text="Add", command=add_details, width=39)
add_button.grid(column=1, row=4, columnspan=2)
search_btn = Button(text="Search", command=search_key, width=20)
search_btn.grid(column=2, row=1)



window.mainloop()