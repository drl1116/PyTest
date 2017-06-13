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
print(man)
print('-----------------------')
print(other)
