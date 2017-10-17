''' Main module '''
from __future__ import absolute_import
import sys
import os
import time
import random
import Bomberman
import Board
import Bomb
from termcolor import colored
#import signal
import Config
import Getch
import Enemy


def game_input():
    ''' input '''
    try:
        inp = getch()
    except:
        inp = ''
    return inp


def construct_board():
    ''' board formation '''
    if (bomber.getlives()) <= 0:
        gamelost()
    os.system('tput reset')
    print(colored(
        "\t\t\t   HARD BOMBERMAN V1 \t\t\t\t\t", "yellow", attrs=["bold"]))
    bomber.makebomber()
    for i in Config.BOMBS:
        i.makebomb()
    for i in Config.ENEMIES:
        i.makeenemy()
    w_val, h_val, x_val = len(Config.ARR[0]), len(Config.ARR), 0
    while x_val < h_val:
        y_val = 0
        while y_val < w_val:
            if Config.ARR[x_val][y_val] == 'E' and True:
                print(colored(Config.ARR[x_val][y_val], "red", attrs=["bold"]), end="")
            elif Config.ARR[x_val][y_val].isdigit() and True:
                print(
                    colored(Config.ARR[x_val][y_val], "blue", attrs=["bold"]), end="")
            elif Config.ARR[x_val][y_val] != '/' and True:
                print(
                    colored(Config.ARR[x_val][y_val], "cyan", attrs=["bold", "dark"]),
                    end="")
            else:
                print(
                    colored(
                        Config.ARR[x_val][y_val], "yellow", attrs=["bold", "dark"]),
                    end="")
            y_val = y_val + 1
        print()
        x_val = x_val + 1

    print(colored("\nLevel:", "green"), colored(Config.LEVEL, "green"))
    print(colored("Game Score:", "green"), colored(Config.SCORE, "green"))
    print(colored("Lives:", "yellow"), colored(
        bomber.getlives(), "magenta", attrs=["bold"]))


def next_LEVEL():
    ''' level increment '''
    Config.ENEMYPUT = True
    Config.CONSWALL = True
    getch = Getch._Getch()
    board = Board.Board()
    bomber = Bomberman.Bomber()
    for i in range(Config.LEVEL + 4):
        Config.ENEMIES.append(Enemy.Enemy())
        Config.ENEMIES[i].setposition(Config.ENEMYSET[i][0],
                                      Config.ENEMYSET[i][1])


def BOMBS_update():
    ''' bombs update '''
    for i in Config.BOMBS:
        if i.checktime(time.time()):
            if bomber.bomberkiller(i):
                bomber.setposition(2, 2)
                bomber.makebomber()
            for j in Config.ENEMIES:
                if j.bomberkiller(i):
                    Config.ENEMIES.remove(j)
                    Config.SCORE = Config.SCORE + 100


def enemy_update():
    ''' enemy update '''
    if not len(Config.ENEMIES):
        Config.LEVEL = Config.LEVEL + 1
        os.system('tput reset')
        print(colored("Next Level", "yellow", attrs=["bold", "dark"]))
        time.sleep(1)
        next_LEVEL()
        if Config.LEVEL > 5:
            print(colored(
                "Yayyy....You won :-)", "green", attrs=["bold", "dark"]))
            sys.exit()
    for i in Config.ENEMIES:
        [x_val, y_val] = i.getposition()
        #[p, q] = bomber.getposition()
        flag = 0
        if i.killbomber(bomber):
            bomber.setposition(2, 2)
            bomber.makebomber()

        if Config.ARR[x_val][y_val + 4] != 'E' and Config.ARR[x_val][y_val + 4].isdigit():
            flag = 1
            move = 1
        elif Config.ARR[x_val][y_val - 4] != 'E' and Config.ARR[x_val][y_val - 4].isdigit():
            flag = 1
            move = 2
        elif Config.ARR[x_val + 2][y_val] != 'E' and Config.ARR[x_val + 2][y_val].isdigit():
            flag = 1
            move = 3
        elif Config.ARR[x_val - 2][y_val] != 'E' and Config.ARR[x_val - 2][y_val].isdigit():
            flag = 1
            move = 0
        if flag == 0:
            move = random.randint(0, 3)

        i.removeenemy()
        if move == 0 and True:
            i.movedown()
        elif move == 1 and True:
            i.moveleft()
        elif move == 2 and True:
            i.moveright()
        elif move == 3 and True:
            i.moveup()
        i.makeenemy()

        if i.killbomber(bomber):
            bomber.setposition(2, 2)
            bomber.makebomber()


def gamelost():
    ''' game lost message '''
    print(colored(
        "Sorry... You lost the game :-(", "red", attrs=["bold", "dark"]))
    print(colored("Better luck next time", "red", attrs=["bold", "dark"]))
    sys.exit()


getch = Getch._Getch()
Config.init()
board = Board.Board()
bomber = Bomberman.Bomber()


def update_fn():
    ''' update '''
    BOMBS_update()
    enemy_update()


for i in range(Config.LEVEL + 4):
    Config.ENEMIES.append(Enemy.Enemy())
    Config.ENEMIES[i].setposition(Config.ENEMYSET[i][0], Config.ENEMYSET[i][1])


def quit_game():
    ''' quit '''
    print(colored(
        "Are you sure you want to quit? (yes/no)",
        "red",
        attrs=["bold", "dark"]))
    try:
        choice = str(input())
    except KeyboardInterrupt:
        sys.exit()
    return choice


while True:
    construct_board()
    try:
        move = game_input()
    except KeyboardInterrupt:
        move = 'q'

    if move == 'q' or move == 'Q':
        choice = quit_game()
        if choice == 'yes' or choice == 'y' or choice == 'Y' or choice == 'YES':
            print("\nThanks for playing")
            time.sleep(1)
            sys.exit()
        elif choice == 'no' or choice == 'n' or choice == 'N' or choice == 'NO':
            continue
    elif move == 'd' or move == 'D':
        bomber.removebomber()
        bomber.moveright()
        bomber.makebomber()
    elif move == 'a' or move == 'A':
        bomber.removebomber()
        bomber.moveleft()
        bomber.makebomber()
    elif move == 's' or move == 'S':
        bomber.removebomber()
        bomber.movedown()
        bomber.makebomber()
    elif move == 'w' or move == 'W':
        bomber.removebomber()
        bomber.moveup()
        bomber.makebomber()
    elif move == 'b' or move == 'B':
        bomb_blast = Bomb.Bomb(bomber, time.time())
        if bomb_blast.gettime() - Config.LEFTBTIME >= 0.5 and True:
            Config.BOMBS.append(bomb_blast)
            Config.LEFTBTIME = bomb_blast.gettime()
            bomb_blast.makebomb()
    update_fn()
