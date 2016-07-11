def txt_reader(file_name):
    txt_lst = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            txt_lst.append(line.split('\t'))
    return txt_lst


def count_games(file_name):
    txt = txt_reader(file_name)
    return(len(txt))


def decide(file_name, year):
    txt = txt_reader(file_name)
    for i in txt:
        if str(year) in i:
            return True
    return False


def get_latest(file_name):
    txt = txt_reader(file_name)
    counter = 0
    game_name = ''
    for i in txt:
        if i[2] > str(counter):
            counter = i[2]
            game_name = i[0]
    return game_name


def count_by_genre(file_name, genre):
    txt = txt_reader(file_name)
    counter = 0
    for i in txt:
        if genre in i:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    txt = txt_reader(file_name)
    counter = 0
    for i in txt:
        counter += 1
        if title in i:
            return counter
    raise ValueError('There is no such game.')


def sort_abc(file_name):
    txt = txt_reader(file_name)
    games = []
    for game in txt:
        games.append(game[0])
    for i in range(len(games)-1, 0,  -1):
        for j in range(i):
            if games[j] > games[j+1]:
                comp = games[j]
                games[j] = games[j+1]
                games[j+1] = comp
    return games


def get_genres(file_name):
    txt = txt_reader(file_name)
    genres = []
    for genre in txt:
        if genre[-2] not in genres:
            genres.append(genre[-2])
    return sorted(genres)   # rpg != real-time --- sorted not working properly


def when_was_top_sold_fps(file_name):
    txt = txt_reader(file_name)
    maxi = 0
    year = ''
    for i in txt:
        if i[3] == 'First-person shooter':
            if float(i[1]) > float(maxi):
                maxi = i[1]
                year = i[2]
    return int(year)
    raise ValueError('No First-person shooter game in the database')
