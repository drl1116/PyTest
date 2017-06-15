# -*- coding: utf-8 -*-
import os
pwd = os.getcwd()
print(pwd)
os.chdir('./chapter')
pwd = os.getcwd()
print(pwd)
print('-----------------------')
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('文件不存在!')

# 利用try/except/finally处理
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('文件错误!')
finally:
    man_file.close()
    other_file.close()

# 使用with重写上部分代码
try:
    with open('man_data1.txt', 'w') as man_file1, open('other_data.txt', 'w') as other_file1:
        print(man, file=man_file1)
        print(other, file=other_file1)
except IOError as err:
    print('文件错误:' + str(err))

os.chdir('D:/DRL/SourceTree/PyTest/Head_First_Python3/chapter')
with open('man_data.txt') as mdf:
    print(mdf.readline())
