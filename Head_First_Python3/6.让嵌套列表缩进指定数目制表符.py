# -*- coding: utf-8 -*-
# nester Version = '1.2.0'


def print_lol(the_list, level=0):
    '''这个函数有一个位置参数,名为"the_list",
    这可以是任何Python列表(包括或不包含嵌套列表),
    所提供列表中的各个数据项会(递归地)打印到屏幕上,而且各占一行.
    第二个参数(名为"level")用来在遇到嵌套列表时插入制表符.
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)


movies = ["The Holy Grail", "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michnel Palin", 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

print_lol(movies, 0)
print('---------------------------')
print_lol(movies, 1)
print('---------------------------')
print_lol(movies, 2)
print('---------------------------')
print_lol(movies, -2)
print('***************************')
names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print_lol(names, -1)
print('***************************')
print_lol(names)
