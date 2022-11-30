# 01
# 查找字符 find
str1 = "大家好，我的名字是:蜗牛"
str_pos = str1.find(':')
print(str1[str_pos + 1:])

# 02
# 查找字符 split
str2 = "大家好，我的名字是:蜗牛，很高兴认识大家"
str2_list = str2.split(':')
str2_split = str(str2_list[1])
str2_split_list = str2_split.split('，')
print(str2_list)
print(str2_split_list)
print(str2_split_list[0])

# 03
user_sex_str = input("请输入你的性别：")
user_height_str = input("请输入你的身高（厘米）：")
user_weight_str = input("请输入你的体重（公斤）：")
# 去除空格和单位
user_sex_str = user_sex_str.replace(' ', '')
user_height_str = user_height_str.replace(' ', '')
user_height_str = user_height_str.replace('厘米', '')
user_weight_str = user_weight_str.replace(' ', '')
user_weight_str = user_weight_str.replace('公斤', '')

user_height = float(user_height_str)
user_weight = float(user_weight_str)

standard_weight = (user_height - 100) * 0.9
if user_sex_str[0] == '女':
    standard_weight -= 2.5

print(f"你的标准体重为{standard_weight}")

if -5 < user_weight - standard_weight < 5:
    print("体重标准，继续保持")
elif standard_weight < (user_weight - 5):
    print("偏胖，多运动")
else:
    print("偏瘦，多吃肉")
