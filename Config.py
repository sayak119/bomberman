''' Global module '''
def init():
    ''' initialization '''

    global BOMBS, ENEMYPUT
    global ENEMIES, SCORE, CONSWALL, CONSBRICK, LEFTBTIME
    global ARR, LEVEL, ENEMYSET

    ARR = [[' ' for x in range(80)] for y in range(42)]
    BOMBS = []
    CONSWALL = True
    SCORE = 0
    CONSBRICK = []
    ENEMIES = []
    ENEMYSET = []
    LEVEL = 1
    ENEMYPUT = True
    LEFTBTIME = 0
