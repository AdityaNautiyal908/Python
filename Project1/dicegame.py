import tkinter as tk
import random
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")


dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image = image1)
label2 = tk.Label(window,image = image2)

label1.image = image1
label2.image = image2

label2.place(x = 40, y = 100)
label2.place(x = 300, y = 100)


window.mainloop()