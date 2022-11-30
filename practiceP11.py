# 01
def check_str_cmp(str1_list, str2_list):
    cmp_list = []
    for i in range(len(str1_list)):  # 遍历第一个列表
        check_name = str1_list[i]
        if check_name != '':
            for j in range(len(str2_list)):  # 遍历第二个列表
                if check_name == str2_list[j]:
                    cmp_list.append(check_name)
    return cmp_list


str1 = """
李明
高裳

刘浩
张帅

黄浩
陈例
"""

str2 = """
刘浩

莉莉

丽莎
张帅

陈例
高航
"""

str1_list = str1.split('\n')
str2_list = str2.split('\n')
print(str1_list)
print(str2_list)
# 两个列表中都有的名字
cmp_name = check_str_cmp(str1_list, str2_list)
print(f'两个列表都存在的名字：{cmp_name}')
print('\n')

# 02 14:30
str3 = """
刘浩,30
莉莉,43
丽莎,19
张帅,18
陈例,34
高航,45
"""

str3_list = str3.splitlines()
str_name_age = []

for i in range(len(str3_list)):
    name_age = str3_list[i].strip()
    if name_age != '':
        str_name_age.append(name_age.split(','))

print(str_name_age)

less_30_list = []
greate_30_list = []

for i in range(len(str_name_age)):
    if int(str_name_age[i][1]) < 30:
        less_30_list.append(str_name_age[i][0])

    else:
        greate_30_list.append(str_name_age[i][0])

print("年龄小于30岁的人:")
for i in range(len(less_30_list)):
    print(less_30_list[i])

print("年龄大于或等于30岁的人:")
for i in range(len(greate_30_list)):
    print(greate_30_list[i])
