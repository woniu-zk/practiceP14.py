# P5练习
# 01
def data_sum(arg1, arg2):
    return (arg1 + arg2)


# sum1 = data_sum(1)    #只有一个实参，错误
sum2 = data_sum(1, 2)
sum3 = data_sum(arg1=1, arg2=10)  # 可以指定参数传入
# sum4 = data_sum(arg1 = 1, 32)   #前面指定参数传入后面不指定参数传入，错误
sum5 = data_sum(1, arg2=83)  # 可以前面不指定参数后面指定参数传入
# sum6 = data_sum(arg2=90)  #只有一个实参，错误

print(f"sum2 = {sum2}")
print(f"sum3 = {sum3}")
print(f"sum5 = {sum5}")


# 02
def age_info(name, age):
    return str(name) + ':' + str(age)


info1 = age_info("黄生", 29)
info2 = age_info(name="关羽", age="28")
print(info1)
print(info2)
