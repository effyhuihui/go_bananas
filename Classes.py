__author__ = 'effy'

## The class is defined to describe all the objects in the program

class Graph(object):
    def __init__(self, x, y):

        """
        :param x:  coordinate of x
        :param y:  coordinate of y
        """
        self.x = x
        self.y = y

    def getX(self):

        """
        the method is to keep in track of the x location
        :return: x location
        """
        return self.x

    def getY(self):

        """
        the method is to keep in track of the y location
        :return:  y location
        """
        return self.y

    def setLocation(self, stepx, stepy):
        """
        set the location of x, y by stepx and stepy
        :param stepx: the stepsize in x axis
        :param stepy: the stepsize in y axis
        """
        self.x += stepx
        self.y += stepy

class Monkey(Graph):
    '''
    inheriate all the methods in Graph Class
    while adding a class variable Life to keep in track of the status of monkey
    '''
    Life = 3

    def reduce_life(self):

        """
        add class variable Life by 1
        """
        Monkey.Life -= 1

    def add_life(self):

        """
        reduce class variable Life by 1
        """
        Monkey.Life += 1