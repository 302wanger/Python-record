fav_movies = ["The Holy grail",["hello",89],["nihao",11], "The life fo brain"]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(fav_movies)
