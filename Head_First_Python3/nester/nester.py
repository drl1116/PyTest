# -*- coding: utf-8 -*-
'''
这是一个测试模块,实现功能是:将嵌套列表的数据全部列出来;
提供了一个名为print_lol()的函数;
'''


def print_lol(the_list):
    '''
    这个函数取一个位置参数,名为"the_list",
    这可以是任何Python列表(也可以是包含嵌套列表的列表).
    所指定的列表中的每个数据项会(递归地)输出到屏幕上,
    各个数据项占一行;
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


'''
查看Python默认模块存放位置,可以打开IDLE输入:
import sys; sys.path
可以得到位置列表;
'''
