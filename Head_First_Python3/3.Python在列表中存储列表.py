# !/usr/bin/python
# -*- coding:utf-8 -*-

# 在列表中存储列表
movies = ["The Holy Grail", "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michnel Palin", 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
# 可以通过中括号记法来访问特定值,下面结果为Eric Idle
print(movies[3][1][3])

# 打印列表值
print(movies)
# 利用for循环打印列表值
for each_item in movies:
    print(each_item)

# 检查某个特定标识符是否包含某个特定类型:isinstance()
names = ['Michael', 'Terry']
isinstance(names, list)
# 输出为True
num_names = len(names)
isinstance(num_names, list)
# 输出为False

print('--------------------------------------------------------')
# 处理一层嵌套列表数据
movies = ["The Holy Grail", "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michnel Palin", 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
print('-------------------------------------------------------')
