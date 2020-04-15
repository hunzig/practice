import json
import pygal
import math
#　将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
dates = []
months = []
weeks = []
weekdays = []
close = []


# 打印每一天的信息
#for btc_dict in btc_data:
#    date = btc_dict['date']
#    month = int(btc_dict['month'])
#    week = int(btc_dict['week'])
#    weekday = btc_dict['weekday']
#    close = int(float(btc_dict['close']))
#    print("{}is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（ｒｍｂ）'
line_chart.x_labels = dates
N = 20 #　ｘ轴坐标每２０天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图(rmb).svg')

    
