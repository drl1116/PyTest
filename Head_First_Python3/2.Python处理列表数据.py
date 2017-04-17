# !/usr/bin/python
# -*- coding: utf-8 -*-
fav_movies = ["The Holy Grail", "The Life of Brian"]

# 普通方式打印列表
print(fav_movies[0])
print(fav_movies[1])

# 用for循环打印列表
fav_movies = ["The Holy Grail", "The Life of Brian"]
for i in fav_movies:
    print(i)

# 用while循环打印列表(需要声明一个初始值)
x = 0
while x < len(fav_movies):
    print(fav_movies[x])
    x = x + 1

'''
Python中常见的一些问题:
1.能用for循环尽量用for循环,少用while循环;
2.Python的列表不支持越界检查,也就是无法访问不存在的数据,否则会提示IndexError;
3.单引号和双引号功能相同;
4.如果要在一个字符串中嵌入一个单引号或双引号可以用 \' 或 \" ;
5.命名只能以字母或下划线开始,后面可以跟数字,字母,下划线,不允许特殊字符;
6.Python是大小写敏感的,所以msg和MSG是两个不同的字符串;报NameError错
'''
