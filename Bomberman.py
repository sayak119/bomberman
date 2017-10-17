''' Bomberman module '''
from __future__ import absolute_import
import Config
from Person import Person


class Bomber(Person):
    ''' contains properties of bomberman and inherits properties of Person class'''
    def __init__(self):
        ''' init fx '''
        Person.__init__(self)
        self.position = [2, 2]
        self.lives = 3
        self.shape = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]

    def makebomber(self):
        ''' bomber formation '''
        [x_val, y_val] = self.getposition()
        i = 0
        while i < 4:
            Config.ARR[x_val][i + y_val] = self.shape[0][i]
            Config.ARR[x_val + 1][i + y_val] = self.shape[1][i]
            i = i + 1

    def removebomber(self):
        ''' deleting bomber '''
        [x_val, y_val] = self.getposition()
        i = 0
        while i < 4:
            Config.ARR[x_val][i + y_val] = ' '
            Config.ARR[x_val + 1][i + y_val] = ' '
            i = i + 1
