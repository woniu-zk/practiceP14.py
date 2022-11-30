# while练习

input_num = 0
num_list = []
i = 0
num_sum = 0

print("输入数字求和，按下q结束\n")

while ( input_num != 'q' ) and ( input_num != 'Q'):
    i += 1
    num_sum += float(input_num)
    input_num = input("请输入第" + str(i) + "位数字：")
    num_list.append(input_num)

i = 0
for get_num in num_list:

    if(get_num != 'q') and (get_num != 'Q'):
        i += 1
        if i != 1:
            print("+")
        print(get_num)

print("=" + str(num_sum))
