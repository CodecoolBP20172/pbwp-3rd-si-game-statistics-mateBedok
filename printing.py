import reports
import pprint
# Printing functions
pp = pprint.PrettyPrinter(width=40, compact=True)
pp.pprint(reports.count_games("game_stat.txt"))
pp.pprint(reports.decide("game_stat.txt", 2000))
pp.pprint(reports.get_latest("game_stat.txt"))
pp.pprint(reports.count_by_genre("game_stat.txt", "RPG"))
pp.pprint(reports.get_line_number_by_title("game_stat.txt", "Diablo II"))
