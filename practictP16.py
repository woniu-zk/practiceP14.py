# -*- coding = utf-8 -*-
# @Time:2022/11/30 14:52
# @Author:蜗牛
# @Site:
# @File:practictP16.py
# @Software:PyCharm

if __name__ == '__main__':
    # 调试
    with open("0016_1.txt", mode='r', encoding='utf-8') as f:
        f_data = f.read().splitlines()
        f_list = []
        for one_data in f_data:
            if not one_data:  # 数据空
                continue
            f_list.append(one_data.split(' '))

        name = []
        temp_name = ''
        max_integral = 0
        cnt = 0
        for i in range(len(f_list)):
            cnt = 0
            for data in f_list[i]:
                if not data:    # 空，跳出
                    continue

                cnt += 1
                if cnt == 1:    # 取名字
                    temp_name = data
                elif cnt == 2:  # 取分数
                    if max_integral < int(data):  # 目前最大分数比表中的小
                        max_integral = int(data)
                        name = [temp_name]
                    elif max_integral == int(data):
                        name.append(temp_name)

        print(f"积分最高的人是：{name},积分值为：{max_integral}")

