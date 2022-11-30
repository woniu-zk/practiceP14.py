# 格式化字符
# 功能:自动写生日祝福
# cur_year = 2022
#
# friend = {"老黄": ("同事", 1993), "黎明": ("老同学", 1997), "高峰": ("朋友", 1990)}
# relation = ["同事", "老同学", "表弟"]
#
# friend_name = input("请输入接收生日祝福的人:")
#
# # 查找朋友列表中是否有这个人
# if friend_name in friend:
#     friend_age = cur_year - friend[friend_name][1]
#     friend_relation = friend[friend_name][0]
#     print("""
#     {0}你好呀，我是你的{1}
#     祝你{2}岁生日快乐
#     """.format(friend_name, friend_relation, friend_age))
# else:
#     print("你的朋友列表中没有这个人")

# 功能：查询成绩
result_report = {"小马": ("语文", 63, "数学", 94, "英语", 30),
                 "刘浩": ("语文", 59, "数学", 63, "英语", 47),
                 "李宝": ("语文", 89, "数学", 85, "英语", 94)}

student_name = input("请输入需要查询的同学成绩单:")
if not(student_name in result_report):
    print("班级中没有该同学")
else:
    chinese_result = result_report[student_name][1]
    math_result = result_report[student_name][3]
    english_result = result_report[student_name][5]

    print(f"""
    {student_name}同学的语文成绩为:{chinese_result}分,
    数学成绩为:{math_result}分,
    英语成绩为:{english_result}分
    """)

