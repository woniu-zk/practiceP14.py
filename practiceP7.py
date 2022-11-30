# 01
var1 = [33, ['我的名字', '蜗牛'], 'hello word']
print(var1[-1])

# 02
print(var1[1][1])  # 打印 蜗牛

# 03
var1[-1] = 'omg'
print(var1)
var1[1][1] = '蜗牛快跑'
print(var1)

# 04
var2 = [33, ('我的名字', '蜗牛'), 'hello word']
var2[1] = ('我的名字', '蜗牛快跑')
print(var2)


# 05
# 函数不会改变传入的值
def func(arg):
    arg = 'hi'


var3 = 'hello'
func(var3)
print(var3)


# 函数会改变传入的值 类似c语言传入数组和指针
def func(arg):
    arg[0] = 'hi'


var4 = ['hello']
func(var4)
print(var4)


def func(arg):
    arg['data1'] = 'hi'


var4 = {'data1': 'hello'}
func(var4)
print(var4)


# 函数不会改变传入的值
def func(arg):
    arg = ['hi']


var5 = ['hello']
func(var5)
print(var5)

# 切片
var6 = ['hi', 'hello', 'my', 'name', 'is', 'woniu']
print(var6[2:])

var7 = ('hi', 'hello', 'my', 'name', 'is', 'woniu')
print(var7[-4:])

var8 = {'data1': '001', 'data2': '002', 'data3': '003'}

print(var8['data2'])
