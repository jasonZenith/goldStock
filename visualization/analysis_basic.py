import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mplfinance.original_flavor import candlestick_ochl
from matplotlib import ticker
import warnings

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
warnings.simplefilter("ignore")


class VisualizingKline:    # 声明：定义一个制作K线的类

    def read_file(self):
        df_stock = pd.read_csv(f'../data_get_deposit/{self}_pr.csv', index_col=[0], dtype={'股票代码': 'str', '交易日期': 'str'})  # 去掉第一列数字列column
        print(df_stock.head(3))     # 打印头三行
        print(df_stock.tail(3))     # 打印尾三行
        df_stock_pr = df_stock.query('交易日期 >= "20200101"').reset_index()
        df_stock_pr = df_stock_pr.sort_values(by='交易日期', ascending=True)  # 创建df_stock_pr接收数据按照日期降序排列的文件
        df_stock_pr['dates'] = np.arange(0, len(df_stock_pr))   # len(df_stock_pr):记录数
        fig, ax = plt.subplots(figsize=(9, 5))
        fig.subplots_adjust(bottom=0.2)
        candlestick_ochl(ax, quotes=df_stock_pr[['dates', '开盘价', '收盘价', '最高价', '最低价', '涨跌额']].values,
                         colorup='r', colordown='g', width=0.65, alpha=0.85)
        dt_tick = df_stock_pr['交易日期'].values

        def fm_d(x):
            if (x < 0) or (x > len(dt_tick)-1):
                return ''
            return dt_tick[int(x)]

        ax.xaxis.set_major_formatter(ticker.FuncFormatter(fm_d))
        # 按一定规则选取并在水平轴上显示时间刻度
        plt.xticks(rotation=15)  # 关于交易日期变量的旋转角度
        ax.set_ylabel('交易价格')
        plt.xlabel('交易日期')
        plt.title(f'{self}的K线图生成如下')
        plt.grid(True)  # 网格效果
        plt.show()


if __name__ == '__main__':
    VisualizingKline.read_file('300760')    # 迈瑞医疗
    VisualizingKline.read_file('000652')    # 泰达股份
    VisualizingKline.read_file('002223')    # 鱼跃医疗
    VisualizingKline.read_file('002030')    # 达安基因
    VisualizingKline.read_file('600196')    # 复星医药


