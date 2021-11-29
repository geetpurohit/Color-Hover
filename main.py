from tkinter import *
from PIL import Image

path = "test2.png"
im = Image.open(path)
coo = im.getbbox()
img_w = coo[2]
img_h = coo[3]

root = Tk()
root.title("RGB Hover")
canvas = Canvas(width=img_w, height=img_h + 30)

canvas.pack()

img = PhotoImage(file = path)
canvas.create_image(0,0, image=img, anchor=NW)

tag = canvas.create_text(5,600,  text="", anchor="nw", font="Times 11")

def moved(event):
    RGBtuple = im.getpixel((event.x, event.y))
    canvas.itemconfigure(tag, text="The RGBA value at coordinate {0} is {1}".format( (event.x, event.y) , RGBtuple ) )

canvas.bind("<Motion>", moved)

mainloop()
