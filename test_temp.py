# author： Jason Zeng
import tushare as ts
import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pyecharts import Page, Bar, Kline, charts
import warnings

warnings.simplefilter('ignore')
token = 'xxxxxxxxxx'  # tushare社区获取token
# ts.set_token(token)
pro = ts.pro_api(token)


def stock_K_plot(ts_code_list):
    page = Page()
    for ts_code in ts_code_list:
        # 1.收集数据，先输出Excel
        # 提取name
        data = pro.stock_basic(ts_code=ts_code)
        name = data.name.values
        # 获得日线数据
        pa = pro.daily(ts_code=ts_code, start_date='20200101')
        # 输出csv文件
        pa.to_csv(ts_code + '日线.csv', header=True, index=False, encoding='utf-8-sig')
        print('输出' + name + '日线.csv成功')

        #   2.数据处理
        #   2.1数据按时间升序
        pa.index = pd.to_datetime(pa.trade_date)
        pa = pa.sort_index()
        # 2.2转为表格型数据
        da = pd.DataFrame(data=pa)
        # 2.3防止vol列有其他类型数据
        da['vol'] = da['vol'].apply(lambda vol: vol if vol > 0 else 0)
        # 2.4将日期转为list格式
        date = da["trade_date"].apply(lambda x: str(x)).tolist()
        # 2.5将oclh转为数组格式
        k_plot_value = da.apply(lambda record: [record['open'], record['close'], record['low'], record['high']],
                                axis=1).tolist()

        # 3.生成 K chart
        kline = Kline()  # 初始化
        kline.add(ts_code + "近5年日K线图",  # 加标题
                  date, k_plot_value,  # 加x轴, y轴
                  is_datazoom_show=True,  # 缩放
                  mark_line=["average"],  # 加均线
                  mark_point=["max", "min"],  # 标记最大最小值
                  mark_point_symbolsize=60)  # 标记点大小
        kline
        # 4.生成交易量 Bar chart
        bar = Bar()
        bar.add("vol", date, da["vol"],
                tooltip_tragger="axis", is_legend_show=False, is_yaxis_show=False, yaxis_max=5 * max(da["vol"]))
        bar
        # # 5.整合 K chart & Bar chart
        # overlap = charts.overlap()
        # overlap.add(kline)
        # a = overlap.add(bar, yaxis_index=1, is_add_yaxis=True)
        # print('输出' + ts_code + '近5年k线图成功')
        # page.add(a)
    page.render()


file = r'./600519贵州茅台.csv'

# 调用csv.reader(),把前面存储的文件对象f作为参数传递给它，并创建一个与文件相关的阅读器对象next
# 模块csv包含函数next(),调用它并将阅读器对象f传递给它，它将返回文件中下一行。
# 下面得到的是文件的第一行。
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])

        dates.append(date)
        highs.append(high)
        lows.append(low)
print(dates)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 填充二者之间的区域
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperature - 2014', fontsize=24)
plt.xlabel('', fontsize=12)
# 绘制斜的日期标签，以免彼此重叠。
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=10)
plt.tick_params(axis='both', labelsize=12)

# 修改坐标的标注
x_ticks = dates[::3]
plt.xticks(x_ticks)
y_ticks = list(range(45, 75, 5))
plt.yticks(y_ticks)

plt.show()

# 输入股票代码list
stock_K_plot(['000001.SZ', '600519.SH', '688981.SH'])
