# -*- coding: utf-8 -*-
import os
pwd = os.getcwd()
print(pwd)
os.chdir('./chapter')
pwd = os.getcwd()
print(pwd)

# 增加判断文件是否存在判断
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    print(data.readline(), end='')
    print('---------------------')
    data.seek(0)

    for each_line in data:
        print(each_line, end='')
    data.close()

    # 按规则分解文本
    data = open('sketch.txt')
    for each_line in data:
        # 利用条件语句解决报错问题
        if not each_line.find('1') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
    data.close()

    # 使用try和except忽略错误代码
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
else:
    print('文件不存在!')
