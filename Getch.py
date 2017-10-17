''' Get input module '''
from __future__ import absolute_import
from __future__ import division
import sys
import tty
import termios
import Config

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

    def doanything(self):
        ''' does nothing '''

    def doessomething(self):
        ''' still does nothing '''


class _GetchUnix:
    """Fetch and character using the termios module."""

    def __init__(self):
        pass

    def __call__(self):
        from select import select

        filedesc = sys.stdin.fileno()
        old_settings = termios.tcgetattr(filedesc)

        try:
            tty.setraw(sys.stdin.fileno())
            [i, o_val, e_val] = select([sys.stdin.fileno()], [], [], 1 - (Config.LEVEL * 5 / 100))
            if i:
                ch_val = sys.stdin.read(1)
            else:
                ch_val = None

        finally:
            termios.tcsetattr(filedesc, termios.TCSADRAIN, old_settings)

        return ch_val

    def jonsnnow(self):
        ''' knows nothing '''

    def nothingpylint(self):
        ''' garbage '''

class _GetchWindows:
    """Fetch a character using the Microsoft Visual C Runtime."""

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        import time

        # Delay timeout to match UNIX behaviour
        time.sleep(1)

        # Check if there is a character waiting, otherwise this would block
        if msvcrt.kbhit():
            return msvcrt.getch()

        else:
            return

    def nothing(self):
        ''' does nothing '''

    def nothingagain(self):
        ''' knows nothing '''

GETCH = _Getch()
