def cfg():
	# INIT CFG File
	CFG = open("settings.cfg", "r")

	# Check lines
	for line in CFG:
		line = line.rstrip()

		# Skip comments and empty lines
		if line != "":
			if (line[0] == "#"):
				continue

			# Split lines
			text = line.split(" ")

			# Propertis
			if text[0] == "version":
				VER = "v" + text[2]

			if text[0] == "special_symbol":
				SPEC = text[2]
				
			if text[0] == "tags_divider":
				TAGDIV = text[2]
			
			if text[0] == "sleeptime":
				SLEEP = text [2]

			if text[0] == "language":
				LANG = text[2]

			if text[0] == "button":
				BUTTON = text[2]

	return BUTTON, LANG, SLEEP, TAGDIV, SPEC, VER

def interface():
	# INIT variables
	BUTTON, LANG, SLEEP, TAGDIV, SPEC, VER = cfg()

	writed = []
	skip = False

	# INIT List File
	LIST = open("TAGS.txt", "r")

	for line in LIST:

		line = line.rstrip()

		if line == SPEC:
			if LANG == "EN":
				print('Coub TAGS Writer', VER)

				print("\nPress Enter to complete filling.")
				while (skip == False):
					TEMP = input()
					if TEMP == "":
						skip = True
					else:
						writed.append(TEMP)

				print('Press', BUTTON, 'to run the script.\n')

			elif LANG == "RU":
				print('Coub ТЕГ Писатель', VER)

				print("\nНажмите Enter для завершения заполнения.")
				while (skip == False):
					TEMP = input()
					if TEMP == "":
						skip = True
					else:
						writed.append(TEMP)

				print('Нажмите', BUTTON, 'для запуска скрипта.\n')

			else:
				print('ERROR: {0} is wrong language'.format(LANG))
				exit()

		else:
			writed.append(line)

	return writed
