# coding:utf-8
#!usr/bin/env python

from ui.play_display import medium_display
from tiles.game.play import create_new_play, get_score
from ui.user_entries import get_user_menu
from life_cycle.play import cycle_play, save_game, restore_game

def threes():
    partie=None
    menu = get_user_menu(partie)
    if menu == 'N':
        partie = create_new_play()
    elif menu == 'L':
        partie = restore_game()
    jeu=False
    while jeu!=True:
        jeu=cycle_play(partie)

        if jeu == False: #Si le menu est séléctionner en pleine partie.
            menu = get_user_menu(partie)
            if menu == 'S':
                save_game(partie)
                return('Partie sauvegarder')
            elif menu == 'Q':
                save_game(create_new_play())
                return('fin du jeu')

        elif jeu == True:
            save_game(create_new_play())
            replay=''
            while replay != 'r' and replay != 'p':
                print('rejouer r/p')
                replay = str(input())
                replay = replay.lower()
            if replay=='r':
                jeu = False
                partie = create_new_play()
            else:
                return('fin du jeu')
        elif jeu == 'Game Over !':
            medium_display(partie['plateau'])
            partie['score'] = get_score(partie['plateau'])
            print('Votre score est de ', partie['score'] , 'points.')
            return jeu


print("     _   _____   _   _        _____   _   _   _____    _____   _____   _____  ")
print("    | | | ____| | | | |      |_   _| | | | | |  _  \  | ____| | ____| /  ___/ ")
print("    | | | |__   | | | |        | |   | |_| | | |_| |  | |__   | |__   | |___  ")
print(" _  | | |  __|  | | | |        | |   |  _  | |  _  /  |  __|  |  __|  \___  \ ")
print("| |_| | | |___  | |_| |        | |   | | | | | | \ \  | |___  | |___   ___| | ")
print("\_____/ |_____| \_____/        |_|   |_| |_| |_|  \_\ |_____| |_____| /_____/ ")

print(threes())