# -*- coding = utf-8 -*-
# @Time:2022/11/30 15:55
# @Author:蜗牛
# @Site:
# @File:practiceP17.py
# @Software:PyCharm

if __name__ == '__main__':
    with open("0016_1.txt", mode='r', encoding='utf-8') as f:
        f_data = f.read().splitlines()

        # 将数据填入列表
        f_list = []
        for one_data in f_data:
            one_data = one_data.strip()
            if not one_data:  # 数据空
                continue
            f_list.append(one_data.split(' '))

        first_name = '' # 姓氏
        name_dis = {}   # 名字字典
        for data in f_list:
            first_name = data[0]
            data[-2] = int(data[-2])
            # 判断姓氏是否在字典中
            if first_name[0] in name_dis:
                name_dis[first_name[0]] += data[-2]
            else:
                name_dis[first_name[0]] = data[-2]

        for name,integral in name_dis.items():
            print(f"{name}:{integral}")