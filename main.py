from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

YELLOW = "#FFF0CE"
BLUE = "#0C356A"
LIGHT_BLUE = "#0174BE"

# ----------------------------PASSWORD GENERATOR------------------------


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbols
    shuffle(password_list)
    main_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, main_password)
    pyperclip.copy(main_password)


# ----------------------------SAVE PASSWORD-----------------------------


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title="Save", message="Are you confirm")

        if is_ok:
            with open(file="my_password", mode="a") as data:
                data.write(f"website: {website}\nemail: {email}\npassword: {password}\n\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP---------------------------------
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="#FFF0CE")

canvas = Canvas(height=200, width=200, bg=YELLOW, highlightthickness=0)

lock_img = PhotoImage(file="C:/Users/nugan/PycharmProjects/day-29/lock1.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Label
name_label = Label(text="     My Pass", font=("Arial Rounded MT Bold", 20), fg=BLUE, bg=YELLOW)
name_label.grid(row=1, column=1)

website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(row=2, column=0)

email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(row=3, column=0)

password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(row=4, column=0)

# Entry
website_entry = Entry(width=51,)
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2)

email_entry = Entry(width=51)
email_entry.insert(index=0, string="nuganthan1@gmail.com")
email_entry.grid(row=3, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=4, column=1)

# Button
password_button = Button(text="Generate Password", command=password_generator, bg=BLUE, fg="white")
password_button.grid(row=4, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
