# -*- coding = utf-8 -*-
# @Time:2022/11/29 15:40
# @Author:蜗牛
# @Site:
# @File:practiceP14.py
# @Software:PyCharm

if __name__ == '__main__':
    import urllib.request

    url = "http://api.k780.com/?app=life.time&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json"
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    print(html)

    html = html.replace('{', '')
    html = html.replace('}', '')
    html = html.replace('"', '')

    html_list = html.split(',')
    print(html_list)

    city = '北京'
    week = ''
    date = ''
    for data in html_list:
        data_list = data.split(':')
        if len(data_list) == 2:
            att = data_list[0]
            val = data_list[1]
            if att == 'week_2':
                week = val
            elif att == 'datetime_2':
                date = val

    print(f"""城市:{city}
    {week}
    {date}
    """)

