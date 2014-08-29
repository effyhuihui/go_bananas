__author__ = 'effy'
import random
import Classes


def generator(feature, featureImage, spread,im,canvas):

    """
    function to generate both back-and front-end object. And it offers the option to set the spread,i.e,the range of the
    randint function.(I use different range to control the probability of different object that will occur)

    :param feature: object list(back-end list)
    :param featureImage: object image list(front-end list)
    :param spread: the range in the function of random.randint
    :param im: which image it will use to represent different object respectively
    :param canvas: will take in the canvas object from the main module
    """
    if 1 == random.randint(1,spread):
        x = random.randint(20,550)
        feature.append(Classes.Graph(x, 20))
        featureImage.append(canvas.create_image(x, 20, image = im))


def monkey_move(monkey, monkeyImage, direction, canvas):

    """
    set the movement of monkey using the function

    :param monkey: the back end monkey object
    :param monkeyImage:  the front-end monkey object
    :param direction: which direction will it go
    :param canvas: takes in canvas from main
    """
    if direction == "left":
        monkey.setLocation(-8, 0)
        canvas.move(monkeyImage, -8, 0)
    if direction == "right":
        monkey.setLocation(8, 0)
        canvas.move(monkeyImage, 8, 0)

def movement(item, itemim, step, canvas):

    """
    set one falling object "one" step further each time

    :param item: the back end monkey object
    :param itemim: the front-end monkey object
    :param step: step size of each object (except pills,every falling object has a stepsize of 10 )
    :param canvas: takes in the canvas object from main
    """
    item.setLocation(0, step)
    canvas.move(itemim, 0, step)


def backEnd_frontEnd_update(items, itemsImage,step, canvas):

    """
    set a list of falling object "one" step further

   :param item: the back end monkey object
    :param itemim: the front-end monkey object
    :param step: step size of each object (except pills,every falling object has a stepsize of 10 )
    :param canvas: takes in the canvas object from main
    """
    for i in range(len(items)):
        movement(items[i], itemsImage[i], step, canvas)

def check_get_item(item, monkey):

    """

    :param item: the back end falling object
    :param monkey: the back end monkey object
    :return: boolvar, whether a collision has happened.
    """
    if item.getY() + 60 >= monkey.getY() and item.getY() <640:
        if item.getX() + 60 >= monkey.getX() and item.getX() < monkey.getX()+ 100:
            return True
        return False
