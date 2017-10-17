''' Bomb module '''
from __future__ import absolute_import
import Config

class Bomb(object):
    '''contains properties of bomb like time to detonate, explosion pattern '''
    def __init__(self, bomber, time):
        ''' init fx '''
        self.time = time
        self.position = bomber.getposition()
        self.shape = [['!', '!', '!', '!'], ['!', '!', '!', '!']]

    def makebomb(self):
        ''' bomb formation '''
        [x_val, y_val] = self.getposition()
        i = 0
        while i < 4:
            Config.ARR[x_val][i + y_val] = self.shape[0][i]
            Config.ARR[x_val + 1][i + y_val] = self.shape[1][i]
            i = i + 1

    def getposition(self):
        ''' bomb position '''
        return self.position

    def gettime(self):
        ''' time fx '''
        return self.time

    def explosion(self):
        ''' area fx '''
        [x_val, y_val] = self.getposition()
        i = 0
        while i < 4:
            if Config.ARR[x_val][y_val - 4] == 'X':
                break
            elif Config.ARR[x_val][y_val - 4] == '/':
                Config.CONSBRICK.remove([x_val, y_val - 4])
                Config.SCORE += 20
            Config.ARR[x_val][i + y_val - 4] = 'e'
            Config.ARR[x_val + 1][i + y_val - 4] = 'e'
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val][y_val + 4] == 'X':
                break
            elif Config.ARR[x_val][y_val + 4] == '/':
                Config.CONSBRICK.remove([x_val, y_val + 4])
                Config.SCORE += 20
            Config.ARR[x_val][i + y_val + 4] = 'e'
            Config.ARR[x_val + 1][i + y_val + 4] = 'e'
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val + 2][y_val] == 'X':
                break
            elif Config.ARR[x_val + 2][y_val] == '/':
                Config.CONSBRICK.remove([x_val + 2, y_val])
                Config.SCORE += 20
            Config.ARR[x_val + 2][i + y_val] = 'e'
            Config.ARR[x_val + 1 + 2][i + y_val] = 'e'
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val - 2][y_val] == 'X':
                break
            elif Config.ARR[x_val - 2][y_val] == '/':
                Config.CONSBRICK.remove([x_val - 2, y_val])
                Config.SCORE += 20
            Config.ARR[x_val - 2][i + y_val] = 'e'
            Config.ARR[x_val + 1 - 2][i + y_val] = 'e'
            i = i + 1

    def explode(self):
        ''' cleaning board '''
        [x_val, y_val] = self.getposition()
        self.time = -1
        i = 0
        while i < 4:
            Config.ARR[x_val][i + y_val] = ' '
            Config.ARR[x_val + 1][i + y_val] = ' '
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val][y_val - 4] == 'X':
                break
            Config.ARR[x_val][i + y_val - 4] = ' '
            Config.ARR[x_val + 1][i + y_val - 4] = ' '
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val][y_val + 4] == 'X':
                break
            Config.ARR[x_val][i + y_val + 4] = ' '
            Config.ARR[x_val + 1][i + y_val + 4] = ' '
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val + 2][y_val] == 'X':
                break
            Config.ARR[x_val + 2][i + y_val] = ' '
            Config.ARR[x_val + 1 + 2][i + y_val] = ' '
            i = i + 1

        i = 0
        while i < 4:
            if Config.ARR[x_val - 2][y_val] == 'X':
                break
            Config.ARR[x_val - 2][i + y_val] = ' '
            Config.ARR[x_val + 1 - 2][i + y_val] = ' '
            i = i + 1

    def timer(self, sp_val):
        ''' timer view '''
        sp_val = str(sp_val)
        self.shape = [[sp_val, sp_val, sp_val, sp_val], [sp_val, sp_val, sp_val, sp_val]]

    def checktime(self, time):
        ''' countdown '''
        bomb_time = 2 - int(time) + int(self.time)
        if bomb_time >= 0 and True:
            if bomb_time:
                self.timer(bomb_time)
            else:
                self.timer('e')
            if bomb_time < 1:
                self.explosion()
            return False
        elif bomb_time < 0:
            self.explode()
            Config.BOMBS.remove(self)
            return True
