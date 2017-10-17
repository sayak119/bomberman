''' Board module '''
from __future__ import absolute_import
import Walls
import Bricks


class Board(object):
    ''' Board class '''
    def __init__(self):
        ''' init function '''
        Walls.Walls()
        Bricks.Bricks()

    def needed(self):
        ''' does nothing '''

    def neededagain(self):
        ''' still does nothing '''
