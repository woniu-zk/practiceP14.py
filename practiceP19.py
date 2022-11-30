# -*- coding = utf-8 -*-
# @Time:2022/11/30 16:53
# @Author:蜗牛
# @Site:
# @File:practiceP19.py
# @Software:PyCharm
import traceback

if __name__ == '__main__':
   with open("0019.txt", mode='rb') as f:
        f_lines = f.read().splitlines()

        line_num = 0
        for data in f_lines:
            line_num+=1
            try:
                data = data.decode('utf-8')
                print(f'第{line_num}行有：{len(data)}个字节的数据')
            except UnicodeDecodeError:
                print(f'第{line_num}行不是"utf-8编码"！！！')
