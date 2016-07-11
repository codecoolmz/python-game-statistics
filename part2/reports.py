def txt_reader(file_name):
    txt_lst = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            txt_lst.append(line.split('\t'))
    return txt_lst


def get_most_played(file_name):
    txt = txt_reader(file_name)
    maxi = 0
    game_name = ''
    for line in txt:
        if float(line[1]) > float(maxi):
            maxi = line[1]
            game_name = line[0]
    return game_name


def sum_sold(file_name):
    txt = txt_reader(file_name)
    solded = 0
    for line in txt:
        solded += float(line[1])
    return solded


def get_selling_avg(file_name):
    txt = txt_reader(file_name)
    counter = 0
    solded = 0
    for line in txt:
        solded += float(line[1])
        counter += 1
    avg_sell = solded / counter
    return avg_sell


def count_longest_title(file_name):
    txt = txt_reader(file_name)
    longest_title = ''
    for line in txt:
        if len(line[0]) > len(longest_title):
            longest_title = line[0]
    return len(longest_title)


def get_date_avg(file_name):
    txt = txt_reader(file_name)
    sum_year = 0
    counter = 0
    for line in txt:
        sum_year += int(line[2])
        counter += 1
    average_year = sum_year / counter
    return round(average_year)


def get_game(file_name, title):
    txt = txt_reader(file_name)
    game_line = []
    for line in txt:
        if title == line[0]:
            game_line = line
            game_line = [i.rstrip() for i in game_line]
            for item in game_line:
                game_line[1] = float(game_line[1])
                game_line[2] = int(game_line[2])
            return game_line


def count_grouped_by_genre(file_name):
    txt = txt_reader(file_name)
    group = {}
    for line in txt:
        if not line[3] in group:
            group[line[3]] = 1
        else:
            group[line[3]] += 1
    return group


def get_date_ordered(file_name):
    txt = txt_reader(file_name)
    txt.sort(key=lambda x: x[0])
    txt.sort(key=lambda x: x[2], reverse=True)
    ordered = []
    for line in txt:
        ordered.append(line[0])
    return(ordered)
print(get_date_ordered('game_stat.txt'))
