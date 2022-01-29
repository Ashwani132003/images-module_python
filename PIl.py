import os
from tkinter import *
from PIL import ImageTk, Image

os.system('cls')

root = Tk()
root.title("images")

my_img = ImageTk.PhotoImage(Image.open("sample_image.jpg"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=1)

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.grid(row=0, column=0)

root.mainloop()