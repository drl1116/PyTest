# -*- coding:utf-8 -*-
# nester Version = '1.3.0'


def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')
            print(each_item)


movies = ["The Holy Grail", "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michnel Palin", 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
print_lol(movies)
print('--------------------------------------------')
print_lol(movies, True)
print('--------------------------------------------')
print_lol(movies, True, 2)
