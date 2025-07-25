from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

# Initialize Tkinter Window
window = Tk()
window.title("Navkis College Of Enginnering")
window.geometry("1920x1080")
window.configure(bg="#093545")

# Canvas Setup
canvas = Canvas(
    window,
    bg="#093545",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Set up paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Venkatesh UR\Videos\z Mini altration\ImageSteganographySystem000\assets\frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Minimize and Maximize Functions
def minimize_window():
    window.iconify()  # Minimize the window

def maximize_window():
    if window.state() == "normal":
        window.state("zoomed")  # Maximize to full screen
    else:
        window.state("normal")  # Restore to normal size

# # Add Minimize Button
# minimize_button = Button(
#     text="—",  # Unicode for the minimize symbol
#     command=minimize_window,
#     bg="#093545",
#     fg="white",
#     borderwidth=0,
#     font=("Arial", 12)
# )
# minimize_button.place(x=1400, y=10, width=20, height=20)
   

# # Add Maximize Button
# maximize_button = Button(
#     text="⬜",  # Unicode for a square symbol
#     command=maximize_window,
#     bg="#093545",
#     fg="white",
#     borderwidth=0,
#     font=("Arial", 12)
# )
# maximize_button.place(x=1425, y=10, width=20, height=20)

# Open Different Interfaces
def open_login_interface():
    window.withdraw()  # Hide the current interface
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def open_encoding_interface():
    window.withdraw()  # Hide the current interface
    subprocess.Popen(["python", "gui4.py"])
    window.destroy()  # Close the current interface

def open_decoding_interface():
    window.withdraw()  # Hide the current interface
    subprocess.Popen(["python", "gui5.py"])
    window.destroy()  # Close the current interface

# Add GUI Elements
# image_image_1 = PhotoImage(
#     file=relative_to_assets("image_1.png"))
# image_1 = canvas.create_image(
#     438.0,
#     474.0,
#     image=image_image_1
# )

# image_image_1 = PhotoImage(
#     file=relative_to_assets("image_1.png"))
# image_1 = canvas.create_image(
#     700.0,
#     700.0,
#     image=image_image_1
# )



canvas.create_text(
    450.0,
    28.0,
    anchor="nw",
    text="Welcome to Iamge Steganography!",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 44 * -1)
)
#encode
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_encoding_interface,
    relief="flat"
)
button_1.place(
    x=670.0,
    y=380.0,
    width=191.0,
    height=69.0
)

#decode
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_decoding_interface,
    relief="flat"
)
button_2.place(
    x=670.0,
    y=480.0,
    width=191.0,
    height=69.0
)


#logout
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_login_interface,
    relief="flat"
)
button_3.place(
    x=1425.0,
    y=30.0,
    width=91.0,
    height=34.0
)

canvas.create_text(
     550.0,
     150.0,
     anchor="nw",
     text="Image Steganography is an System that enables you",
     fill="#FFFFFF",
     font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    570.0,
    185.0,
    anchor="nw",
    text="to hide secret messages within digital images.",
    fill="#FFFFFF",
    font=("Arial", 20 * -1)
)

canvas.create_text(
    560.0,
    300.0,
    anchor="nw",
    text="  Please choose one of the following features::-",
    fill="#FFFFFF",
    font=("Arial", 20 * -1)
)

# Enable Window Resizing
window.resizable(True, True)
window.mainloop()
