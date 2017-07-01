
# Export functions


import reports
import csv


def export_file(file_name):
    file = open(file_name, "w", newline='')
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    data = [reports.get_most_played("game_stat.txt"),
            reports.sum_sold("game_stat.txt"),
            reports.get_selling_avg("game_stat.txt"),
            reports.count_longest_title("game_stat.txt"),
            reports.get_date_avg("game_stat.txt"),
            reports.get_game("game_stat.txt", "Minecraft"),
            reports.count_grouped_by_genre("game_stat.txt"),
            reports.get_date_ordered("game_stat.txt")]
    for answer in data:
        writer.writerow([answer])
    file.close()
