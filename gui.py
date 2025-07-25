
from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3
import bcrypt

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
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Venkatesh UR\Videos\z Mini altration\ImageSteganographySystem000\assets\frame0")
# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_register_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui2.py"])
    window.destroy()  # Close the current interface

#Authentication
def authenticate():
    username = entry_1.get()
    password = entry_2.get()

    canvas.itemconfig(error_text, text="")  # Clear previous error messages
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)

    # Query the database to check if the credentials are correct
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]
        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw ( password.encode(), hashed_password ) :
            # Authentication successful, open the home page
            open_home_interface()
        else:
            # Authentication failed, show an error message
            canvas.itemconfig ( error_text, text = "Incorrect username or password",font=("Arial", 14) )
            canvas.coords(error_text, 625, 550)  # Update position for this message

    else:
        # Authentication failed, show an error message
        canvas.itemconfig(error_text, text="Incorrect username or password",font=("Arial", 14))
        canvas.coords(error_text, 625, 550)  # Update position for this message



'''
# Retrieve the users and their passwords from the database
cursor.execute("SELECT username, password FROM users")
users = cursor.fetchall()
for user in users:
    username, password = user
    print("Username:", username)
    print("Password:", password)
    print()

#delete all of the users
cursor.execute("DELETE FROM users")
connection.commit()
'''

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    438.0,
    474.0,
    image=image_image_1
)

# Create the error text widget
error_text = canvas.create_text(
    320.0,
    380.0,
    anchor="nw",
    fill="#FF0000",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= authenticate,
    relief="flat"
)
button_1.place(
    x=634.0,
    y=610.0,
    width=256.0,
    height=34.0
)
#We Realized that we need a register button in the login page
button_image = PhotoImage(
    file=relative_to_assets("Button.png"))
button = tk.Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command= open_register_interface,
    relief="flat"
)
button.place(
    x=1425.0,
    y=30.0,
    width=91.0,
    height=34.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    758.0,
    362.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial", 16)  # Specify font and size here

)
entry_1.place(
    x=610.0,
    y=344.0,
    width=300.0,
    height=34.0
)

canvas.create_text(
    727.0,
    300.0,
    anchor="nw",
    text="Login ID:",
    fill="#FFFFFF",
    font=("Poppins Regular", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    758.0,
    500.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial", 18),  # Specify font and size here
    show="*"
)
entry_2.place(
    x=608.0,
    y=485.0,
    width=300.0,
    height=34.0
)

canvas.create_text(
    727.0,
    438.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    500.0,
    200.0,
    anchor="nw",
    text="Welcome to Image Steganography, login to your account in order to access",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    700.0,
    101.0,
    anchor="nw",
    text="Log in",
    fill="#FFFFFF",
    font=("Poppins Regular", 40 * -1)
)
window.resizable(True, True)
window.mainloop()
