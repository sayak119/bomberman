''' Bricks module '''
from __future__ import absolute_import
import random
import Config


class Bricks(object):
    ''' contains properties of bricks and their shape'''
    def __init__(self):
        ''' init fx '''
        if Config.CONSWALL:
            h_val = len(Config.ARR)
            w_val = len(Config.ARR[0])
            x_val = 4
            while x_val < h_val - 2:
                y_val = 6
                while y_val < w_val - 2:
                    if random.randint(0, 1) and random.randint(
                            0, 1) and random.randint(0, 2) and True:
                        if Config.ARR[x_val][y_val] == ' ':
                            Config.CONSBRICK.append([x_val, y_val])
                    y_val = y_val + 4
                x_val = x_val + 2

            Config.CONSWALL = False
            if Config.ENEMYPUT:
                for i in range(Config.LEVEL + 4):
                    coll = random.choice(Config.CONSBRICK)
                    Config.ENEMYSET.append(coll)
                    Config.CONSBRICK.remove(coll)
                Config.ENEMYPUT = False

        for i in Config.CONSBRICK:
            ax_val = [0, 1, 2, 3, 4]
            j = 0
            while ax_val[j] < 4:
                Config.ARR[i[0]][ax_val[j] + i[1]] = '/'
                Config.ARR[i[0] + 1][ax_val[j] + i[1]] = '/'
                j = j + 1

    def nagain(self):
        ''' pylint doesn't know what's best '''

    def nagainagain(self):
        ''' min-public-methods=2 by default '''
