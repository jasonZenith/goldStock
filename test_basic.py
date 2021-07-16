# author： Jason Zeng
import tushare as ts
import json
import pandas as pd
import warnings

warnings.simplefilter('ignore')
token = 'xxxxxxxxxx'  # tushare社区获取token
pro = ts.pro_api(token)


def get_Stock(stock_code):
    df = pro.daily(ts_code=stock_code, start_date='20200101', end_date='20200331')
    # df = pd.DataFrame(df)
    # 选择时间段2020年初爆发疫情最近3个月为例
    columns_change = '{"ts_code":"股票代码","trade_date":"交易日期","open":"开盘价","high":"最高价","low":"最低价","close":"收盘价",' \
                     '"pre_close":"昨日收盘价","change":"涨跌额","pct_chg":"涨跌幅","vol":"成交量","amount":"成交额"} '
    columns_changes = json.loads(columns_change)
    df.rename(columns=columns_changes, inplace=True)
    # df.dropna(axis=0, how='', inplace=True)
    stock_name = stock_code[:6]
    csv_name = stock_name + '_pr.csv'
    df.to_csv(csv_name)

    print(stock_name + "预处理" + ':\n', df)


if __name__ == '__main__':
    get_Stock('300760.SZ')  # 迈瑞医疗
    get_Stock('000652.SZ')  # 泰达股份
    get_Stock('002223.SZ')  # 鱼跃医疗
    get_Stock('002030.SZ')  # 达安基因
    get_Stock('600196.SH')  # 复星医药
