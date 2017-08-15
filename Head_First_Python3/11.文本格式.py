# -*- coding: utf-8 -*-
import os
import sys
print(os.getcwd())
os.chdir('D:\DRL\PyTest\Head_First_Python3/chapter')
print(os.getcwd())
print('----------------------------------------')


# 定义一个print_lol函数,列表显示数据
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=fh)
            print(each_item, file=fh)


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

# 使用print_lol函数打印显示
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
print()
