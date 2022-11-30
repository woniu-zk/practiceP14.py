# 类的使用
# 成绩系统
# class StudentResult:
#     def __init__(self, name, ident):
#         self.name = name
#         self.id = ident
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}
#
#     def set_grades(self, course, grade):
#         if course in self.grades:
#             self.grades[course] = grade
#         else:
#             print("没有该科目")
#
#     def disp_grades(self):
#         print(f"{self.name} (学号{self.id})的成绩:")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}")
#
#
# student1 = StudentResult("小马", 10)
# student1.set_grades("语文", 98)
# student1.set_grades("英语", 85)
# student1.disp_grades()

# 猫咪信息管理
class Cat:
    def __init__(self, name):
        self.name = name
        self.attr = {"颜色": "橙色", "品种": "橘猫", "重量": "3kg", "出生日期": "2022.11.11", "喜好": "睡觉"}

    def set_attr(self, attr, val):
        if attr in self.attr:
            self.attr[attr] = val
        else:
            print("没有该属性")

    def get_attr(self, attr):
        if attr in self.attr:
            return self.attr[attr]
        else:
            print("没有该属性")


my_cat = Cat("蜗牛")
my_cat.set_attr("颜色", "米黄")
my_cat.set_attr("品种", "狸花猫")

print(f"我的猫叫{my_cat.name},是一只{my_cat.get_attr('颜色')}的{my_cat.get_attr('品种')}")

