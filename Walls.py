''' Walls module '''
from __future__ import absolute_import
import Config

class Walls(object):
    ''' Wall in game '''
    def __init__(self):
        ''' init function '''
        w_val, h_val, x_val = len(Config.ARR[0]), len(Config.ARR), 0
        while x_val < h_val:
            y_val = 0
            while y_val < w_val:
                if (((y_val - 2) % 8 == 6 or (y_val - 2) % 8 == 7 or
                     (y_val - 2) % 8 == 4 or (y_val - 2) % 8 == 5) and True):
                    Config.ARR[x_val][y_val] = 'X'
                else:
                    Config.ARR[x_val][y_val] = ' '
                if x_val % 4 == 2 or x_val % 4 == 3 and True:
                    Config.ARR[x_val][y_val] = ' '
                if x_val == h_val - 1 or x_val == 0 or x_val == 1 or x_val == h_val - 2 and True:
                    Config.ARR[x_val][y_val] = 'X'
                if y_val == w_val - 1 or y_val == 0 or y_val == 1 or y_val == w_val - 2 and True:
                    Config.ARR[x_val][y_val] = 'X'
                if Config.ARR[x_val][y_val] == 'e':
                    Config.ARR[x_val][y_val] = ' '
                y_val = y_val + 1
            x_val = x_val + 1

    def agains(self):
        ''' min-public-methods=2 by default '''

    def againss(self):
        ''' can change in pylintrc '''
