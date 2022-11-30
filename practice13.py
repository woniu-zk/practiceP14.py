# -*- coding = utf-8 -*-
# @Time:2022/11/29 14:42
# @Author:蜗牛
# @Site:
# @File:practice13.py
# @Software:PyCharm

if __name__ == '__main__':
    # 读取文件内容
    f = open("txt_practice13.txt", mode="r", encoding="utf-8")
    file_str = f.read()
    print(file_str)
    f.close()

    # 将内容转换为列表
    file_list = file_str.splitlines()
    name_age_list = []
    for i in range(len(file_list)):
        name_age = file_list[i].replace(' ', '')  # 清除前后空格
        if name_age != '':  # 清除空字符
            name_age_list.append(name_age.split('：'))

    print(name_age_list)

    # 根据年龄分类
    greater_age50_name = "大于50岁的人："
    less_age50_name = "小于或者等于50岁的人："

    for i in range(len(name_age_list)):
        if int(name_age_list[i][1]) > 50:
            greater_age50_name += name_age_list[i][0] + '，'
        else:
            less_age50_name += name_age_list[i][0] + '，'

    print(greater_age50_name)
    print(less_age50_name)

    # 写入文件
    with open("txt_practice13.txt", mode="a", encoding="utf-8") as f:
        f.write('\n')
        f.write(greater_age50_name)
        f.write('\n')
        f.write(less_age50_name)
