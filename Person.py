''' Person module '''
from __future__ import absolute_import
import Config

class Person(object):
    ''' contains properties which are common to both bomberman and enemy'''

    def __init__(self):
        ''' init fx '''
        self.lives = 1
        self.position = ['', '']
        self.shape = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

    def getlives(self):
        ''' player life '''
        return self.lives

    def getposition(self):
        ''' player position '''
        return self.position

    def setposition(self, x_val, y_val):
        ''' fix player '''
        self.position = [x_val, y_val]

    def moveright(self):
        ''' move right '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            bomb = Config.ARR[x_val][y_val + 4] != 'E' and Config.ARR[x_val][y_val
                                                                             + 4].isdigit() and True
            if (bomb or 'X' in Config.ARR[x_val][y_val + 4]
                    or '/' in Config.ARR[x_val][y_val + 4]
                    or 'e' in Config.ARR[x_val][y_val + 4]) and True:
                self.setposition(x_val, y_val)
            else:
                self.setposition(x_val, y_val + 4)
            j = j + 1

    def moveleft(self):
        ''' move left '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            bomb = Config.ARR[x_val][y_val - 4] != 'E' and Config.ARR[x_val][y_val
                                                                             - 4].isdigit() and True
            if (bomb or 'X' in Config.ARR[x_val][y_val - 4]
                    or '/' in Config.ARR[x_val][y_val - 4]
                    or 'e' in Config.ARR[x_val][y_val - 4]) and True:
                self.setposition(x_val, y_val)
            else:
                self.setposition(x_val, y_val - 4)
            j = j + 1

    def moveup(self):
        ''' move up '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            bomb = Config.ARR[x_val - 2][y_val] != 'E' and Config.ARR[x_val
                                                                      - 2][y_val].isdigit() and True
            if (bomb or 'X' in Config.ARR[x_val - 2][y_val]
                    or '/' in Config.ARR[x_val - 2][y_val]
                    or 'e' in Config.ARR[x_val - 2][y_val]) and True:
                self.setposition(x_val, y_val)
            else:
                self.setposition(x_val - 2, y_val)
            j = j + 1

    def movedown(self):
        ''' move down '''
        [x_val, y_val] = self.getposition()
        i = [0, 1, 2, 3, 4]
        j = 0
        while i[j] < 4:
            bomb = Config.ARR[x_val + 2][y_val] != 'E' and Config.ARR[x_val
                                                                      + 2][y_val].isdigit() and True
            if (bomb or 'X' in Config.ARR[x_val + 2][y_val]
                    or '/' in Config.ARR[x_val + 2][y_val]
                    or 'e' in Config.ARR[x_val + 2][y_val]) and True:
                self.setposition(x_val, y_val)
            else:
                self.setposition(x_val + 2, y_val)
            j = j + 1

    def death(self):
        ''' player death '''
        self.lives = self.lives - 1

    def bomberkiller(self, bomb):
        ''' kill enemy '''
        [x_val1, y_val1] = bomb.getposition()
        [x_val, y_val] = self.getposition()
        if x_val1 == x_val and y_val1 != y_val and True:
            if abs(y_val1 - y_val) <= 4:
                self.death()
                return True
        if y_val1 == y_val and x_val1 != x_val and True:
            if abs(x_val1 - x_val) <= 2:
                self.death()
                return True
        return False
