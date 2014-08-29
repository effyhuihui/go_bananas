__author__ = 'effy'
from tkinter import *
from PIL import Image,ImageTk
import functions
import  Classes
from tkinter import messagebox
import startPage

"""
The following statements are to open  images for future use,as well as create root, canvas,along with
other global variables
"""
root = Tk()
root.geometry("600x690")

##open image for pills and create lists for both back-end and front-end object respectively
pills = []
pillsImage = []
pillTemp = Image.open("pill.jpg")
pillim = ImageTk.PhotoImage(pillTemp)

##open image for cakes(banana) and create lists for both back-end and front-end object respectively
cakes = []
cakesImage = []
cakeTemp = Image.open("banana.jpg")
cakeim = ImageTk.PhotoImage(cakeTemp)

##open image for poisons and create lists for both back-end and front-end object respectively
poisons = []
poisonsImage = []
poisonTemp = Image.open("Poison.png")
poisonim =ImageTk.PhotoImage(poisonTemp)

##open image for bullets(stone) and create lists for both back-end and front-end object respectively
bullets = []
bulletsImage = []
bulletTemp = Image.open("stone.png")
bulletim = ImageTk.PhotoImage(bulletTemp)

##open image for monkey
monkeyTemp = Image.open("Monkey94.PNG")
monkeyim = ImageTk.PhotoImage(monkeyTemp)

##create canvas
canvas = Canvas(width = 600, height = 660, bg ="white")

## Open and draw hearts image to represent life status,create image list to store items
heartTemp = Image.open("heart.jpg")
heartim = ImageTk.PhotoImage(heartTemp)
heartsImage = []
for i in range(3):
    heartsImage.append(canvas.create_image(580 - 30*i, 30, image = heartim))

##create Monkey object under the class of Monkey
monkey = Classes.Monkey (300,600)
monkeyImage = canvas.create_image(300, 600,image = monkeyim )

##global variable to record Points and the status of the program(either pause or not.)
POINT = 0
PAUSED = False

##widget class
class App(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid(sticky=E) ##the sticky=W argument prompt all widget to the very left side of the column
        self.createWidget()

    def createWidget(self):


        """
        create stop button to flip the PAUSED status.
        Point label to show the updated points in a real time manner.A StringVar type of variable is needed for the label.
        """
        self.title = Label (self,text = "Your got ",)
        self.title.grid(row = 0, column = 1, columnspan = 3)

        self.points = StringVar()
        self.points.set(POINT)
        self.pointsLabel = Label (self, textvariable = self.points)
        self.pointsLabel.grid(row = 0, column = 4)

        self.title2 = Label(self, text = "bananas!!!")
        self.title2.grid(row = 0, column = 5)

        self.stop = Button(self,text = "stop?!", command = self.stop)
        self.stop.grid(row = 0, column = 6)


    def stop(self):

        """
        refer to PAUSED in the global scope so it can be changed.
        pop-up messagebox to control whether to return to the game or quit
        """
        global PAUSED
        PAUSED = not PAUSED
        if messagebox.askyesno("Game Paused", "Resume, or Quit?"):
            PAUSED = not PAUSED
        else:
            root.destroy()

def key(event):
    """
    control the key event , similarly the global variable PAUSED needs to be referred in here.

    """
    global  PAUSED

    ## Player can move Monkey within the canvas.
    if event.keysym == "Left" and not PAUSED:
        if monkey.getX() > 50:
            functions.monkey_move(monkey,monkeyImage, "left", canvas)

    if event.keysym == "Right" and not PAUSED:
        if monkey.getX() < 540:
            functions.monkey_move(monkey,monkeyImage,"right", canvas)

    ## when up key is pressed, create both front-end and back-end bullets,and they will be generated from the head of
    ## the Monkey.
    if event.keysym == "Up" and not PAUSED:
        bx = monkey.getX() + 20
        bullets.append(Classes.Graph(bx, 550))
        bulletsImage.append(canvas.create_image(bx, 550, image =bulletim))

    canvas.update()


def timer():
    """
    first: randomly generate three items, or not.
    secondly: move both backend item and frontend item
    thirdly: check a: whether get cake(Y-->Point+1;destroy cake)
                   b: whether get poisons(Y-->Life-1;destroy poison)
                   c: whether shoot poison(Y-->destroy both poison and bullet,create 4 bananas)
                   d:whether get pills(Y-->Life+1)
    """
    global PAUSED
    global POINT
    global root

    if not PAUSED:

        ## if the game is not paused,the first step is to do the generating "decision".(whether an object will be
        ## generated this time, and if so, where is the location.)
        functions.generator(cakes, cakesImage, 20,cakeim, canvas)
        functions.generator(poisons, poisonsImage, 50, poisonim, canvas)
        functions.generator(pills, pillsImage , 150, pillim, canvas)

        ## after generating is done, move both the back-end and front-end of the object for 10 pixels(pills are faster)
        functions.backEnd_frontEnd_update(poisons, poisonsImage, 10, canvas)
        functions.backEnd_frontEnd_update(cakes, cakesImage, 10, canvas)
        functions.backEnd_frontEnd_update(bullets, bulletsImage, -10, canvas)
        functions.backEnd_frontEnd_update(pills, pillsImage, 15, canvas)

        ## check if there is any collision between poisons and bullets are going on for the moment.Do a reverse check in
        ## the list(step=-1),so that the changing length of the list will no result in IndexError
        for i in range(len(bullets)-1, -1, -1):
            bX = bullets[i].getX()
            bY = bullets[i].getY()
            for j in range(len(poisons)-1, -1, -1):
                pX = poisons[j].getX()
                pY = poisons[j].getY()
                ##collision check
                if bX + 50 >= pX >= bX -50:
                    if bY + 50 >= pY >= bY - 50:
                        ##if collided,remove both front-and back-end of the object.
                        canvas.delete(bulletsImage[i])
                        canvas.delete(poisonsImage[j])
                        del bullets[i],bulletsImage[i], poisons[j], poisonsImage[j]
                        ## create four bananas on canvas.
                        for k in range(4):
                            cakesImage.append(canvas.create_image(pX-15*(k-2), pY- 15 * (k-2), image = cakeim))
                            cakes.append(Classes.Graph(pX-15*(k-2),pY- 15 * (k-2)))

        ## same happens for cakes(bananas),do a reversed check throughout the list,to see whether Monkey get cakes
        for i in range(len(cakes)-1, -1, -1):
            ##if the cake(banana) is outside of the canvas,delete it.
            if cakes[i].getY() >= 640:
                canvas.delete(cakesImage[i])
                del cakes[i], cakesImage[i]
            ## only check cakes(bananas) whose Y is greater than 550(when the two objects are adjacent to each other),
            ## cuz monkey can not move vertically, that's where the collision could happen for the first time.
            ## if it happens ,delete all related objects in the lists,and set the new POINT to the above StringVar,
            ## update the label.
            elif cakes[i].getY()>=550 and functions.check_get_item(cakes[i], monkey):
                canvas.delete(cakesImage[i])
                del cakes[i], cakesImage[i]
                POINT += 1
                main.points.set(POINT)
                root.update_idletasks()

        ## same happens for poisons check.reversed check
        for i in range(len(poisons)-1, -1, -1):
            if poisons[i].getY() >= 640:
                canvas.delete(poisonsImage[i])
                del poisons[i], poisonsImage[i]
            elif poisons[i].getY() >= 550 and functions.check_get_item(poisons[i],monkey):
                canvas.delete(poisonsImage[i])
                del poisons[i],poisonsImage[i]
                monkey.reduce_life()

                ## if monkey has less than 0 life, the game is over(and the heartsList will be empty)
                if monkey.Life>=0:
                    canvas.delete(heartsImage[len(heartsImage) - 1])
                    del heartsImage[len(heartsImage) - 1]
                else:
                    messagebox.showinfo("Game over!!", "You are poisoned to death,but you got {} bananas!!!".format(POINT))
                    root.destroy()

        ## check whether get the pills
        for i in range(len(pills)-1, -1, -1):
            if pills[i].getY() >= 640:
                canvas.delete(pillsImage[i])
                del pills[i], pillsImage[i]
            ##if a pill is get,monkey's life and herat image will be added by one
            elif pills[i].getY() >= 550 and functions.check_get_item(pills[i],monkey):
                canvas.delete(pillsImage[i])
                del pills[i], pillsImage[i]
                monkey.add_life()
                heartsImage.append(canvas.create_image(580 - 30*len(heartsImage), 30, image = heartim))

    root.after(60, timer)

## initialize the widget class object
main = App(root)

if __name__ == "__main__":
    ## force into the loop where startpage will be called.Whenever "start" button is clicked(Value=0), quit the loop.
    while 1:
        startPage
        if startPage.app.VALUE == 0:
            break

    ## use the input value from startpage to fill out the title of the window, and call everything to make the event
    ## loop working.

    root.title("Welcome! {} !".format(startPage.app.username))
    root.grid()
    canvas.grid()
    canvas.bind("<Key>", key)
    canvas.focus_set()

    timer()
    root.mainloop()

