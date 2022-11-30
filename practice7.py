import time

cur_time = time.localtime()
# print("当前时间为:" + str(cur_time))
print(cur_time)
year = cur_time[0]
month = cur_time[1]
data = cur_time[2]
hour = cur_time[3]
mim = cur_time[4]
sec = cur_time[5]
print(f"""
{year}年
{month}月{data}日
{hour}:{mim}:{sec}
""")

