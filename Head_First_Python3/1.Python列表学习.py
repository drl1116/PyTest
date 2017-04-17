# !/usr/bin/python
# -*- coding: utf-8 -*-

# 建立列表
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# 计算列表数据项
print(len(movies))

# 显示列表第二个项
print(movies[1])

# 显示整个列表内容
print(movies)

# 给列表添加一个项
movies.append("Gilliam")
print(movies)

# 删除列表第四项
movies.pop(3)
print(movies)

# 给列表添加一个数据集合
movies.extend(["Hello World", "Play Game"])
print(movies)
print(len(movies))

# 在列表中删除一个特定的数据项
movies.remove("Play Game")
print(movies)
print(len(movies))

# 在某个特定数据项前增加一个数据项
movies.insert(0, "Chapman")
print(movies)

# 在Movies列表每项后,填入年代数据
movies.pop()
movies.pop(0)
print(movies)
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)

# 直接生成完整列表
movies = ["The Holy Grail", 1975, "The Life of Brian",
          1979, "The Meaning of life", 1983]
print(movies)
