# coding=gbk   防止SyntaxError: Non-UTF-8 code
import tushare as ts
import json
import warnings
warnings.simplefilter('ignore')
token = 'xxxxxxxxxx'  # tushare社区获取token
pro = ts.pro_api(token)


def get_Plate(stock_code):
    df = pro.ths_daily(ts_code=stock_code, start_date='20200101', end_date='20200331',
                       fields='ts_code,trade_date,change')

    columns_change = '{"ts_code":"板块代码","trade_date":"交易日期","change":"涨跌额"} '
    columns_changes = json.loads(columns_change)
    df.rename(columns=columns_changes, inplace=True)
    # df.dropna(axis=0, how='', inplace=True)
    # stock_name = stock_code[:6]
    csv_name = '医疗器械概念涨跌_pr.csv'
    df.to_csv(csv_name)

    print("医疗器械概念涨跌情况预处理" + ':\n', df)


if __name__ == '__main__':
    get_Plate('885539.TI')  # 医疗器械概念板块
