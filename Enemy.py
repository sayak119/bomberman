''' Enemy module '''
from __future__ import absolute_import
import random
import Config
from Person import Person


class Enemy(Person):
    '''contains properties of ENEMIES and inherits Person class'''
    def __init__(self):
        ''' init fx '''
        Person.__init__(self)
        self.position = [7, 2]
        self.motion = random.randint(0, 3)
        self.lives = 1
        self.shape = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]

    def getdirection(self):
        ''' motion fx '''
        return self.motion

    def makeenemy(self):
        ''' enemy formation '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            Config.ARR[x_val][i[j] + y_val] = self.shape[0][i[j]]
            Config.ARR[x_val + 1][i[j] + y_val] = self.shape[1][i[j]]
            j = j + 1

    def removeenemy(self):
        ''' enemy deletion '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            Config.ARR[x_val][i[j] + y_val] = ' '
            Config.ARR[x_val + 1][i[j] + y_val] = ' '
            j = j + 1

    def killbomber(self, bomber):
        ''' bomber killing '''
        [x_val1, y_val1] = bomber.getposition()
        [x_val, y_val] = self.getposition()
        if x_val1 == x_val and y_val1 == y_val and True:
            bomber.death()
            return True
        else:
            return False
