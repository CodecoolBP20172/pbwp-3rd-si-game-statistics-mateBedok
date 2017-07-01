
# Printing functions


import reports
import pprint


pp = pprint.PrettyPrinter(indent=3, width=80, compact=True)
pp.pprint(reports.get_most_played("game_stat.txt"))
pp.pprint(reports.sum_sold("game_stat.txt"))
pp.pprint(reports.get_selling_avg("game_stat.txt"))
pp.pprint(reports.count_longest_title("game_stat.txt"))
pp.pprint(reports.get_date_avg("game_stat.txt"))
pp.pprint(reports.get_game("game_stat.txt", "Minecraft"))
pp.pprint(reports.count_grouped_by_genre("game_stat.txt"))
pp.pprint(reports.get_date_ordered("game_stat.txt"))
