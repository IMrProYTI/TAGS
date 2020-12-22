def interface():
    from config import LANG, button
    version = "v0.5"

    if LANG == "EN":
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
        print("Press button for use script:", button)

        return [[name1, name2, name3],[track1, track2, track3]]

    elif LANG == "RU":
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
        print("Кнопка для использования скрипта:", button)

        return [[name1, name2, name3],[track1, track2, track3]]

    elif LANG == "DEBUG":
        print('TAGS writer', version)

        name1 = "name1"
        name2 = "name2"
        name3 = "name3"

        track1 = "track1"
        track2 = "track2"
        track3 = "track3"

        print()
        print("Press button for use script:", button)

        return [[name1, name2, name3],[track1, track2, track3]]

    else:
        print('ERROR: {0} is wrong language'.format(LANG))
        exit()
