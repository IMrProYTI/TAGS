from keyboard import is_pressed, write, send
from time import sleep
from os import system
import config

status = False
version = "v0.5"
TAGS = open("TAGS.txt", "r")
system("mode con cols=65 lines=15")

if config.LANG == "EN":
    print('TAGS writer', version)

    print()
    print('Name anime/film:')
    name1 = input('First variant of name: ')
    name2 = input('Second variant of name: ')
    name3 = input('Third variant of name: ')

    print()
    print('Name of track:')
    track1 = input('First variant of name: ')
    track2 = input('Second variant of name: ')
    track3 = input('Third variant of name: ')

    print()
    print("Press button for use script:", config.button)

if config.LANG == "RU":
    print('TAGS писатель', version)

    print()
    print('Название аниме/фильма:')
    name1 = input('Первый вариант названия: ')
    name2 = input('Второй вариант названия: ')
    name3 = input('Третий вариант названия: ')

    print()
    print('Название трека:')
    track1 = input('Первый вариант названия: ')
    track2 = input('Второй вариант названия: ')
    track3 = input('Третий вариант названия: ')

    print()
    print("Кнопка для использования скрипта:", config.button)

if config.LANG == "DEBUG":
    name1 = "name1"
    name2 = "name2"
    name3 = "name3"

    track1 = "track1"
    track2 = "track2"
    track3 = "track3"

    print("Press button for use script:", config.button)

while True:
    if is_pressed(config.button):
        status = True

    if status == True:
        status = False
        for line in TAGS:
            line = line.rstrip()
            if line == '$':
                if name1 != "":
                    write(name1) # name1
                    send("tab")
                    sleep(0.1)
                if name2 != "":
                    write(name2) # name2
                    send("tab")
                    sleep(0.1)
                if name3 != "":
                    write(name3) # name3
                    send("tab")
                    sleep(0.1)

                if track1 != "":
                    write(track1) # track1
                    send("tab")
                    sleep(0.1)
                if track2 != "":
                    write(track2) # track2
                    send("tab")
                    sleep(0.1)
                if track3 != "":
                    write(track3) # track3
                    send("tab")
                    sleep(0.1)
            else:
                write(line)
                send("tab")
                sleep(0.1)
        TAGS.close()
        if config.LANG == "RU":
            print('Программа закроеться через 10 секунд.')
            sleep(10)
            exit()
        if config.LANG == "EN" or config.LANG == "DEBUG":
            print('Program close after 10 seconds.')
            sleep(10)
            exit()
