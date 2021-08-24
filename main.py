from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = user_entry.get()
    pw = password_entry.get()

    if len(website) == 0 or len(pw) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oups",
                            message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Do you want to add the following details? \nEmail/username: {email} \nPassword: {pw}")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} || {email} || {pw}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry()
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "ponjae11@gmail.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate_pw)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(width=35, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
