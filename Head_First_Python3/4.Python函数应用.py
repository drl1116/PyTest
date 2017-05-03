# !/usr/bin/python
# -*- coding: utf-8 -*-
# 还是上面那个例子,这次采用函数解决
movies = ["The Holy Grail", "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michnel Palin", 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

# 利用函数解决多层嵌套列表数据


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


# 调用递归函数(Python中默认递归深度不超过100)
print_lol(movies)

# 两个重要的BIF:len()和isinstance()
# len()用来统计数据长度
a = 'kjhasfkljhbaSLKJFBlakshfdlkAHSDKJHalkshdKAJHSDFAL'
b = len(a)
print(b)

# isinstance()用来检查数据类型
c = 'tiyhoiusahofi'
d = 5677
e = isinstance(c, str)
f = isinstance(d, float)
print(e, f)
