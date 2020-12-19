from keyboard import is_pressed, write, wait, send
from time import sleep
from os import system
import config

status = False
version = "v0.4"
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
    print("config.button for use script:", config.button)

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

    print("Кнопка для использования скрипта:", config.button)


while True:
    if is_pressed(config.button):
        status = True

    if status == True:
        status = False
        write("anime") # amine
        send("tab")
        sleep(0.1)
        write("music") # music
        send("tab")
        sleep(0.1)
        write("coub") # coub
        send("tab")
        sleep(0.1)
        write("b100r") # b100r
        send("tab")
        sleep(0.1)
        write("anime coub") # anime coub
        send("tab")
        sleep(0.1)
        write("music coub") # music coub
        send("tab")
        sleep(0.1)
        write("anime music coub") # anime music coub
        send("tab")
        sleep(0.1)
        write("edm") # edm
        send("tab")
        sleep(0.1)
        write("electronic") # electronic
        send("tab")
        sleep(0.1)
        write("electro music") # electro music
        send("tab")
        sleep(0.1)
        write("electronic music") # electronic music
        send("tab")
        sleep(0.1)
        write("electro dance music") # electro dance music
        send("tab")
        sleep(0.1)
        write("electronic dance music") # electronic dance music
        send("tab")
        sleep(0.1)
        write("emotional music") # emotional music
        send("tab")
        sleep(0.1)
        write("art") # art
        send("tab")
        sleep(0.1)
        write("amv") # amv
        send("tab")
        sleep(0.1)
        write("edit") # edit
        send("tab")
        sleep(0.1)
        write("amv coub") # amv coub
        send("tab")
        sleep(0.1)
        write("amv edit") # amv edit
        send("tab")
        sleep(0.1)
        write("loop") # loop
        send("tab")
        sleep(0.1)
        write("loops") # loops
        send("tab")
        sleep(0.1)
        write("looped") # looped
        send("tab")
        sleep(0.1)
        write("song loop") # song loop
        send("tab")
        sleep(0.1)
        write("music loop") # music loop
        send("tab")
        sleep(0.1)
        write("looped coub") # looped coub
        send("tab")

        if name1 != "":
            write(name1) # name1s
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

        write("never existed.")
        send("tab")

        if config.LANG == "RU":
            print('Программа закроеться через 10 секунд.')
            sleep(10)
            exit()
        if config.LANG == "EN":
            print('Program close after 10 seconds.')
            sleep(10)
            exit()
wait()
#
