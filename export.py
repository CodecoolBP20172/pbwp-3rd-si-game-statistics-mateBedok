
# Export functions

import reports
import csv


def export_file(file_name):
    file = open(file_name, "w", newline='')
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    data = [reports.count_games("game_stat.txt"), reports.decide("game_stat.txt", 2000)
            , reports.get_latest("game_stat.txt"), reports.count_by_genre("game_stat.txt", "RPG")
            , reports.get_line_number_by_title("game_stat.txt", "Terraria")]
    for answer in data:
        writer.writerow([answer])
    file.close()
