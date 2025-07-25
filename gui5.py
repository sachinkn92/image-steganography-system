
from pathlib import Path
import tkinter as tk

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import subprocess
from PIL import Image

window = Tk()
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
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Venkatesh UR\Videos\z Mini altration\ImageSteganographySystem000\assets\frame5")
global selected
def open_login_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def open_encoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui4.py"])
    window.destroy()  # Close the current interface

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_decoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui5.py"])
    window.destroy()  # Close the current interface

def handle_enter(event):
    entry_1.insert(tk.END, "\n")  # Insert a newline character when Enter is pressed

def open_file_dialog():
    global selected
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        selected = Image.open(file_path)
        entry_1.delete(0, tk.END)  # Clear the current text in the Entry widget
        entry_1.insert(0, file_path)  # Insert the selected file path into the Entry widget

#decryption
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - int(''.join(filter(str.isdigit, key)))) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - int(''.join(filter(str.isdigit, key)))) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

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

canvas.create_text(
    496.0,
    28.0,
    anchor="nw",
    text="Decoding with Image Steganography!",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 36 * -1)
)

canvas.create_text(
    639.0,
    104.0,
    anchor="nw",
    text="1. Choose the Encrypted image",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    661.0,
    135.0,
    anchor="nw",
    text="2. Decode the message",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    770.0,
    285.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial",16*-1)
)
entry_1.place(
    x=625.0,
    y=270.0,
    width=280.0,
    height=35.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_2 = canvas.create_image(
    770.0,
    425.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Arial",16*-1)
)

from steganography_functions import decode_lsb

global decoded_message
decoded_message=''
def decode_photo():
    if selected is not None:
        image_path = entry_1.get()
        key = entry_2.get()
        # Perform encoding using the selected photo
        decoded_message = decode_lsb(selected)
        final = decrypt(decoded_message, key)
        canvas.itemconfig(Final_text, text=final)

# Create the error text widget
# decrypted text
Final_text = canvas.create_text(
    790.0,
    590.0,
    anchor="nw",
    fill="#B3E5FC",
    font=("Poppins Regular", 20 * -1)
)
'''entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_3 = canvas.create_image(
    431.0,
    350.5,
    image=entry_image_3
)'''

canvas.create_text(
    480.0,
    590.0,
    anchor="nw",
    text="Here you find your hidden message :",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

#print("The hidden message is : ",final)
entry_2.place(
    x=628.0,
    y=407.0,
    width=280.0,
    height=35.0,
    
)

"""image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    541.0,
    167.0,
    image=image_image_2
)"""

button_image_locate = PhotoImage(
    file=relative_to_assets("image_2.png"))
button_locate = Button(
    image=button_image_locate,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_dialog,
)

button_locate.place(
    x=900.0,
    y=277.0,
)

canvas.create_text(
    734.0,
    226.0,
    anchor="nw",
    text="Locate ...",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    670.0,
    360.0,
    anchor="nw",
    text="Enter the Encryption code :",
    fill="#FFFFFF",
    font=("Poppins Regular", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_home_interface,
    relief="flat"
)
button_1.place(
    x=1425.0,
    y=30.0,
    width=91.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=decode_photo,
    relief="flat"
)
button_2.place(
    x=635.0,
    y=490.0,
    width=115.0,
    height=37.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_decoding_interface,
    relief="flat"
)
button_3.place(
    x=796.0,
    y=490.0,
    width=115.0,
    height=37.0
)
window.resizable(True, True)
window.mainloop()
