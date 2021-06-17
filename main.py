from keyboard import is_pressed, write, send
from interface import interface
from time import sleep
from os import system
import config

# Константы
status = False
TAGS = open("TAGS.txt", "r")
system("mode con cols=70 lines=15")

# Вызов текстового интерфейса
name1, name2, name3, track1, track2, track3 = interface()

# Тело
while True:
    # Статус заданой кнопки
    if is_pressed(config.button):
        status = True

    # Проверка статуса и выполнение команд
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
        # Завершающий диалог
        TAGS.close()
        if config.LANG == "RU":
            print('Программа закроеться через 10 секунд.')
            sleep(10)
            exit()
        if config.LANG == "EN" or config.LANG == "DEBUG":
            print('Program close after 10 seconds.')
            sleep(10)
            exit()
