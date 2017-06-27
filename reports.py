# Report functions


def count_games(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        return(len(im_list))


def decide(file_name, year):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        if str(year) in im_str:
            return True
        else:
            return False


def get_latest(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        year_list = {}
        for elements in im_list[0:]:
            elements = elements.split("\t")
            year_list[elements[0]] = (elements[2])
    value_list = list(year_list.values())
    key_list = list(year_list.keys())
    return(key_list[value_list.index(max(value_list))])


def count_by_genre(file_name, genre):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        return(im_str.count(genre))


def get_line_number_by_title(file_name, title):
    not_in_list = True
    with open(file_name, "r") as im_file:
        for num, line in enumerate(im_file, 1):
            if title in line:
                not_in_list = False
                return num
        if not_in_list:
            raise ValueError


# Bonus


def sort_abc(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        title_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            title_list.append(elements[0])
    return sorted(title_list)


def get_genres(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        genre_list = []
        for elements in im_list[0:]:
            elements = elements.split("\t")
            genre_list.append(elements[3])
        for n, genre in enumerate(genre_list):
            if genre == "RPG":
                genre_list[n] = "Rpg"
        genre_list = sorted(set(genre_list))
        for n, i in enumerate(genre_list):
            if i == "Rpg":
                genre_list[n] = "RPG"
        return genre_list


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as im_file:
        im_str = im_file.read().strip()
        im_list = im_str.split("\n")
        year_list = {}
        for elements in im_list[0:]:
            elements = elements.split("\t")
            if elements[3] == "First-person shooter":
                year_list[elements[2]] = float(elements[1])
    value_list = list(year_list.values())
    key_list = list(year_list.keys())
    return int(key_list[value_list.index(max(value_list))])
