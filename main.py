from keyboard import is_pressed, write, send
from interface import interface
from time import sleep
from os import system
import config

status = False
TAGS = open("TAGS.txt", "r")
system("mode con cols=70 lines=15")

NAMES = interface()

name1 = NAMES[0][0]
name2 = NAMES[0][1]
name3 = NAMES[0][2]

track1 = NAMES[1][0]
track2 = NAMES[1][1]
track3 = NAMES[1][2]

while True:
    if is_pressed(config.button):
        status = True

    if status == True:
        status = False
        for line in TAGS:
            line = line.rstrip()
            if line == config.special_symbol:
                if name1 != "":
                    write(name1) # name1
                    send(config.tags_divider)
                    sleep(config.sleeptime)
                if name2 != "":
                    write(name2) # name2
                    send(config.tags_divider)
                    sleep(config.sleeptime)
                if name3 != "":
                    write(name3) # name3
                    send(config.tags_divider)
                    sleep(config.sleeptime)

                if track1 != "":
                    write(track1) # track1
                    send(config.tags_divider)
                    sleep(config.sleeptime)
                if track2 != "":
                    write(track2) # track2
                    send(config.tags_divider)
                    sleep(config.sleeptime)
                if track3 != "":
                    write(track3) # track3
                    send(config.tags_divider)
                    sleep(config.sleeptime)
            else:
                write(line)
                send(config.tags_divider)
                sleep(config.sleeptime)
        TAGS.close()
        if config.LANG == "RU":
            print('Программа закроеться через 10 секунд.')
            sleep(10)
            exit()
        if config.LANG == "EN" or config.LANG == "DEBUG":
            print('Program close after 10 seconds.')
            sleep(10)
            exit()
