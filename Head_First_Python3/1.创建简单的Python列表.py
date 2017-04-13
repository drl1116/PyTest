# -*-coding=utf-8-*-

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
