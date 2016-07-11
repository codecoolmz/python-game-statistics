import reports

'''file_name = 'game_stat.txt'
year = 2000
genre = "First-person shooter"
title = "Counter-Strike"'''   # uncomment for testing

report = open("report.txt", "w")
report.write(str(reports.count_games(file_name)) + "\n")
report.write(str(reports.decide(file_name, year)) + "\n")
report.write(str(reports.get_latest(file_name)) + "\n")
report.write(str(reports.count_by_genre(file_name, genre)) + "\n")
report.write(str(reports.get_line_number_by_title(file_name, title)) + "\n")
report.write(str(reports.sort_abc(file_name)) + "\n")
report.write(str(reports.get_genres(file_name)) + "\n")
report.write(str(reports.when_was_top_sold_fps(file_name)) + "\n")
report.close()
