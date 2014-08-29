__author__ = 'effy'

from tkinter import *
from PIL import Image, ImageTk

## create all the necessary object to form a window.
root = Tk()
root.title("Welcome to GO BANANAS!!!")
root.geometry("500x450")
root.grid()

## open image for the background
bg_start = Image.open("start.jpg")
BG_Start = ImageTk.PhotoImage(bg_start)

intro1Temp = Image.open("intro1.png")
intro1im = ImageTk.PhotoImage(intro1Temp)

intro2Temp = Image.open("intro2.png")
intro2im = ImageTk.PhotoImage(intro2Temp)

canvas = Canvas(width=500, height=500,bg="white")
canvas.create_image(120,130,image=BG_Start)
canvas.create_image(380,100,image = intro2im)
canvas.create_image(335,310,image = intro1im)
## widget class
class App(Frame):
    VALUE = 1
    def __init__(self,master):
        super().__init__(master)
        self.grid(sticky = W)

        self.username = ""

        self.lbl = Label (self,text="Your Name?")
        self.lbl.grid(row = 0, column = 0, columnspan =1)

        self.username = Entry(self)
        self.username.grid(row=0, column=1, columnspan = 1)

        self.createWidget()

    def createWidget(self):
        self.start = Button(self,text = "start!!", command = self.start )
        self.start.grid(row = 0,column = 2)

    ## this method will be used to get name for further use
    def get_name(self):
        return self.username.get()

    ## control method to decide whether to quit the startPage loop
    def start(self):
        self.username = self.get_name()
        App.VALUE = 0
        root.destroy()


app = App(root)
canvas.grid()
root.mainloop()





