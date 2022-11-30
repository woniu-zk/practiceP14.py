# 03 格式化字符串 对齐
info = [
    ['user1', 345.6, '黄金'],
    ['user2', 2345.6, '白银'],
    ['user3555', 453.2, '钻石']
]

for i in range(len(info)):
    print(f"用户：{info[i][0]:<10}，积分：{info[i][1]:>6}，段位：{info[i][2]}")
