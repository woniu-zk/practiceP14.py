# 文件操作
f = open("./test.txt", "a", encoding="utf-8")
# print(f.read())   # 读完

# print(f.read(14))    # 读取9个字节

# print(f.readline())
# print(f.readline(2))

# for text in f.readlines():
#     print(text)

f.write("测试1\n")
f.write("测试2\n")
f.writelines("测试3\n")

f.close()
