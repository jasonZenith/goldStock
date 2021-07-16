import tushare as ts
import json
import warnings

warnings.simplefilter('ignore')

token = 'xxxxxxxxxx'  # tushare社区获取token
pro = ts.pro_api(token)


def get_Stock_Turnover(stock_code):
    df = pro.daily_basic(ts_code=stock_code, start_date='20200101', end_date='20200331',
                         fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
    columns_change1 = '{"ts_code":"股票代码","trade_date":"交易日期","turnover_rate":"换手率","volume_ratio":"量比","pe":"市盈率",' \
                      '"pb":"市净率"} '
    columns_changes1 = json.loads(columns_change1)
    df.rename(columns=columns_changes1, inplace=True)
    stock_name = stock_code[:6]
    df.to_csv(stock_name + "turn_pr" + '.csv')
    print(stock_name + "预处理" + "turn" + ':\n', df)


if __name__ == '__main__':
    get_Stock_Turnover('300760.SZ')  # 迈瑞医疗
    get_Stock_Turnover('000652.SZ')  # 泰达股份
    get_Stock_Turnover('002223.SZ')  # 鱼跃医疗
    get_Stock_Turnover('002030.SZ')  # 达安基因
    get_Stock_Turnover('600196.SH')  # 复星医药
