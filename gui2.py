from pathlib import Path
import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3
import bcrypt
import re


window = tk.Tk()
window.title("Navkis College Of Engineering")
window.geometry("1920x1080")
window.configure(bg = "#093545")


canvas = Canvas(
    window,
    bg = "#093545",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Venkatesh UR\Videos\z Mini altration\ImageSteganographySystem000\assets\frame2")
#database creation
# Connect to the database
connection = sqlite3.connect('database.db')
# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)''')




#Registration for new user
def register():
    username = entry_1.get()
    password = entry_2.get()

    canvas.itemconfig(error_text, text="")  # Clear previous error messages
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)

    # Encrypt the password
    hashed_password = bcrypt.hashpw ( password.encode (), bcrypt.gensalt () )
    # Check if the username already exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result[0] > 0: 
        canvas.itemconfig(error_text, text="Username already exists. Please choose a different username.",font=("Arial", 14))
        canvas.coords(error_text, 510, 550)  # Update position for this message
        return

    # Check the length of the password
    if len(password) <= 8:
        canvas.itemconfig(error_text, text="Password should be more than 8 characters long...",font=("Arial", 14))
        canvas.coords(error_text, 560, 550)  # Update position for this message

        return

    # Check if the password meets the requirements
    if not re.match ( r"^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()_+=\-[\]{};':\"\\|,.<>/?])", password ) :
        canvas.itemconfig ( error_text, text = "Password should contain at least one letter, one digit, and one special symbol.",font=("Arial", 14) )
        canvas.coords(error_text, 440, 550)  # Update position for this message
        return

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    connection.commit()
    canvas.itemconfig(success_text, text="Registration successful.",font=("Arial", 14))

    open_login_interface()

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_login_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    438.0,
    474.0,
    image=image_image_1
)
#error text defintion
# Create the error text widget
error_text = canvas.create_text(
    272.0,
    400.0,
    anchor="nw",
    fill="#FF0000",
    font=("Poppins Regular", 12 * -1)
)
success_text = canvas.create_text(
    272.0,
    400.0,
    anchor="nw",
    fill="#00FF00",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= register,
    relief="flat"
)
button_1.place(
    x=635.0,
    y=610.0,
    width=256.0,
    height=34.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("rounded_entry_bg.png"))
entry_bg_1 = canvas.create_image(
    760.5,
    350.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial", 18)  # Specify font and size here

)
entry_1.place(
    x=610.0,
    y=333.0,
    width=300.0,
    height=34.0
)

canvas.create_text(
    720.0,
    290.0,
    anchor="nw",
    text="Username:",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("rounded_entry_bg.png"))
entry_bg_2 = canvas.create_image(
    760.5,
    500.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    show="*",
    font=("Arial", 18)  # Specify font and size here

)
entry_2.place(
    x=610.0,
    y=485.0,
    width=300.0,
    height=34.0
)

canvas.create_text(
    720.0,
    440.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    510.0,
    136.0,
    anchor="nw",
    text="Welcome to Iamge Steganography, Register now and start your trial!",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    600.0,
    165.0,
    anchor="nw",
    text="or login if you already have an account!",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    625.0,
    30.0,
    anchor="nw",
    text="Register Now",
    fill="#FFFFFF",
    font=("Poppins Regular", 44 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= open_login_interface,
    relief="flat"
)
button_2.place(
    x=1425.0,
    y=30.0,
    width=91.0,
    height=34.0
)
window.resizable(True, True)
window.mainloop()
