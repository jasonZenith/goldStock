import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
warnings.simplefilter("ignore")


def read_file(stock_code):
    df_1 = pd.read_csv(f'../data_get_deposit/{stock_code}turn_pr.csv', index_col=0)  # 去掉第一列数字列column
    print(df_1.head())

    def ana_1():
        sns.set_style('whitegrid')
        sns.set(palette='muted', color_codes=True, font='SimHei', font_scale=0.8)   # 设置网格以及解决中文无法显示
        fig, axes = plt.subplots(1, 2)
        sns.distplot(df_1['市盈率'], ax=axes[0], kde=True, rug=True) #  kde:密度曲线  rug:边际毛毯 
        plt.title(f'{stock_code}的市盈图生成如下,市净图生成如下')
        sns.distplot(df_1['市净率'], ax=axes[1], kde=True, rug=True)

        sns.pairplot(df_1, vars=['换手率'], palette='husl')
        plt.title(f'{stock_code}的换手直方图生成如下(2020-01-01至2020-03-31)')
        plt.show()

    ana_1()


if __name__ == '__main__':
    read_file('300760')
    read_file('000652')
    read_file('002223')
    read_file('002030')
    read_file('600196')


    # plt.title()
    # sns.distplot(df_1['换手率'], ax=axes[2], kde=True, rug=True)  #  kde 密度曲线  rug 边际毛毯  
    # sns.distplot(df_1['市净率'], ax=axes[0], kde=True, rug=True)  #  kde 密度曲线  rug 边际毛毯  
    # sns.displot(df_1['市盈率'], ax=axes[1], shade=True)  #  shade  阴影                         
    # sns.displot(df_1['市净率'], ax=axes[1], shade=True)  #  shade  阴影 
    # sns.boxplot(x="换手率", y="市盈率", data=df_1, whis=[0, 100])