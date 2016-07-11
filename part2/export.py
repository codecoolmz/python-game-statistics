import reports

'''file_name = 'game_stat.txt'
title = "Counter-Strike"'''   # uncomment for testing

report_part2 = open("report_part2.txt", "w")
report_part2.write(str(reports.get_most_played(file_name)) + "\n")
report_part2.write(str(reports.sum_sold(file_name)) + "\n")
report_part2.write(str(reports.get_selling_avg(file_name)) + "\n")
report_part2.write(str(reports.count_longest_title(file_name)) + "\n")
report_part2.write(str(reports.get_date_avg(file_name)) + "\n")
report_part2.write(str(reports.get_game(file_name, title)) + "\n")
report_part2.write(str(reports.count_grouped_by_genre(file_name)) + "\n")
report_part2.write(str(reports.get_date_ordered(file_name)) + "\n")
report_part2.close()
