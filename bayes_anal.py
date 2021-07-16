# coding=gbk
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# author: Jason  Zeng

def bayes(stock_name):
    plate_df = pd.read_csv('../data_get_deposit/医疗器械概念涨跌_pr.csv')  # 读取板块指数的文件
    df = pd.read_csv(f'../data_get_deposit/{stock_name}_pr.csv')  # 读取个股数据的文件

    up = 0  # 板块上涨的次数
    same = 0  # 板块不涨不跌的次数
    down = 0  # 板块下跌的次数

    up1 = 0  # 个股上涨的次数
    same1 = 0  # 个股不涨不跌的次数
    down1 = 0  # 个股下跌的次数

    up2 = 0  # 个股上涨的前提下板块上涨的次数
    up3 = 0  # 个股不涨不跌的前提下板块上涨的次数
    up4 = 0  # 个股下跌的前提下板块上涨的次数

    for i in range(len(plate_df)):
        if plate_df.涨跌额[i] > 0:  # 板块指数上涨
            up += 1
        elif plate_df.涨跌额[i] == 0:  # 板块指数不涨不跌
            same += 1
        elif plate_df.涨跌额[i] < 0:  # 板块指数下跌
            down += 1

    # 求P(A) 医疗器械板块上涨的概率
    p_up = up / (i + 1)  # 板块上涨的概率
    print("医疗器械概念板块上涨的概率 P(A)：", p_up)

    # 求P(B) 个股上涨或下跌的概率
    for j in range(len(df)):
        if df.涨跌额[j] > 0:  # 个股上涨
            if plate_df.涨跌额[j] > 0:
                up2 += 1
            up1 += 1
        elif df.涨跌额[j] == 0:  # 个股不涨不跌
            if plate_df.涨跌额[j] > 0:
                up3 += 1
            same1 += 1
        elif df.涨跌额[j] < 0:  # 个股下跌
            if plate_df.涨跌额[j] > 0:
                up4 += 1
            down1 += 1
    p_up1 = up1 / (j + 1)  # 个股上涨的概率
    p_same1 = same1 / (j + 1)  # 个股不涨不跌的概率
    p_down1 = down1 / (j + 1)  # 个股下跌的概率
    print(f"{stock_name}上涨的概率 P(B)：", p_up1)
    print(f"{stock_name}不变的概率：", p_same1)
    print(f"{stock_name}下跌的概率：", p_down1)

    # 求P(A|B=1)，以p_up2表示
    p_up2 = up2 / up1
    # 求P(A|B=0)，以p_same2表示
    if same1 != 0:
        p_same2 = up3 / same1
    else:
        p_same2 = 0
    # 求P(A|B=-1)，以p_down2表示
    p_down2 = up4 / down1

    # P(B|A) = P(A|B)*P(B)/P(A)
    p_up_final = (p_up2 * p_up1) / p_up  # P(B=1|A) = P(A|B)*P(B)/P(A), 以p_same_final表示
    if same1 != 0:
        p_same_final = (p_same2 * p_same1) / p_up   # P(B=0|A) = P(A|B)*P(B)/P(A), 以p_same_final表示
    else:
        p_same_final = 0    # P(B=0|A) = P(A|B)*P(B)/P(A), 以p_same_final表示
    p_down_final = (p_down2 * p_down1) / p_up    # P(B=-1|A) = P(A|B)*P(B)/P(A), 以p_down_final表示
    print(f"{stock_name}上涨时，板块上涨的概率 P(A|B=1)：", p_up2)
    print(f"{stock_name}上涨时，板块上涨的概率 P(A|B=0)：", p_same2)
    print(f"{stock_name}下跌时，板块上涨的概率 P(A|B=-1)：", p_down2)
    print("P(B=1|A) = P(A|B)*P(B)/P(A):", p_up_final)
    print("P(B=0|A) = P(A|B)*P(B)/P(A):", p_same_final)
    print("P(B=-1|A) = P(A|B)*P(B)/P(A):", p_down_final, '\n')
    return p_up_final, p_same_final, p_down_final


if __name__ == '__main__':
    bayes('300760')  # 迈瑞医疗
    bayes('000652')  # 泰达股份
    bayes('002223')  # 鱼跃医疗
    bayes('002030')  # 达安基因
    bayes('600196')  # 复星医药
