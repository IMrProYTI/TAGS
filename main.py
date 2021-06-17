from keyboard import is_pressed, write, send
from time import sleep
from os import system
import func

# INIT Functions
TAGS = func.interface()

FUN = func.cfg()
SLEEP = float(FUN[2])
BUTTON = FUN[0]
LANG = FUN[1]

# INIT variables
status = False

while True:
	# Status of button
	if is_pressed(BUTTON):
		status = True

	# Check and run script
	if status == True:
		status = False
		for tag in TAGS:
			write(tag)
			send("TAB")
			sleep(SLEEP)

		# Завершающий диалог
		if LANG == "RU":
			print('Программа закроеться через 5 секунд.')
			sleep(5)
			exit()
		if LANG == "EN":
			print('Program close after 5 seconds.')
			sleep(5)
			exit()
