import tushare as ts
import warnings

warnings.simplefilter('ignore')
token = 'xxxxxxxxxx'  # tushare社区获取token
pro = ts.pro_api(token)


def get_Plate(stock_code):
    df = pro.ths_daily(ts_code=stock_code, start_date='20200101', end_date='20200331')
    # df = pd.DataFrame(df)
    # 选择时间段2020年初爆发疫情最近3个月

    csv_name = '医疗器械概念_pr.csv'
    df.to_csv(csv_name)

    print("医疗器械概念预处理" + ':\n', df)


if __name__ == '__main__':
    get_Plate('885539.TI')  # 医疗器械概念板块
