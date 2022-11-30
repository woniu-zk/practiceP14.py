# 类继承
class Employee:
    def __init__(self, name, ident, salary):
        self.info = {ident: (name, salary)}
        self.work_time = 0  # 当月工作时间
        self.month_salary = 0   # 当月工资

    def set_work_time(self, time):
        self.work_time = time

    def count_month_salary(self, ident, salary):
        if ident in self.info:
            self.month_salary = salary
            print(f"{self.info[ident][0]}这个月工资为{self.month_salary:.2f}")
            return self.month_salary
        else:
            print("没有该编号的员工")

    def print_into(self):
        print(f"{self.name}(id号:{self.id})")


class FullTimeEmployee(Employee):
    def print_month_salary(self, ident):
        self.month_salary = float(self.info[ident][1]) / 30 * self.work_time
        self.count_month_salary(ident, self.month_salary)


class PartTimeEmployee(Employee):
    def print_month_salary(self, ident):
        self.month_salary = float(self.info[ident][1]) * self.work_time
        self.count_month_salary(ident, self.month_salary)


employee1 = FullTimeEmployee("小马", 2, 8900)
employee1.set_work_time(23)
employee1.print_month_salary(2)

employee2 = PartTimeEmployee("小刘", 3, 100)
employee2.set_work_time(28)
employee2.print_month_salary(3)
