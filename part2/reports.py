
# Report functions


def get_most_played(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        game_list = {}
        for elements in im_list[0:]:
            elements = elements.split("\t")
            game_list[elements[0]] = float(elements[1])
    value_list = list(game_list.values())
    key_list = list(game_list.keys())
    return key_list[value_list.index(max(value_list))]


def sum_sold(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        sold_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            sold_list.append(float(elements[1]))
        return sum(sold_list)


def get_selling_avg(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        return sum_sold("game_stat.txt") / len(im_list)


def count_longest_title(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        sold_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            sold_list.append(len(elements[0]))
        return max(sold_list)


def get_date_avg(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        date_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            date_list.append(float(elements[2]))
        return(-(-sum(date_list) // len(date_list)))


def get_game(file_name, title):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        game_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            elements[1] = float(elements[1])
            elements[2] = int(elements[2])
            game_list.append(elements)
        for num, line in enumerate(game_list):
            if title in line:
                return game_list[num]


def count_grouped_by_genre(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        grouped_list = list(set([]))
        for elements in im_list[0:]:
            elements = elements.split("\t")
            grouped_list.append(elements[3])
        grouped_dict = {}
        for num, genre in enumerate(grouped_list):
            grouped_dict[grouped_list[num]] = im_str.count(genre)
        return grouped_dict


def get_date_ordered(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        date_dict = {}
        for elements in im_list[0:]:
            elements = elements.split("\t")
            date_dict[elements[0]] = int(elements[2])
        srtd_dict = sorted(date_dict.items(), key=lambda t: t[::-1])
    return(srtd_dict)
