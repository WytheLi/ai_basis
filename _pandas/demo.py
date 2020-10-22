import numpy as np
import pandas as pd

# 创建一个符合正太分布的500个股票504天的涨跌幅数据 数组
stock_day_rise = np.random.normal(0, 1, (500, 504))

# 使用Pandas中的数据结构
df_stock_day_rise = pd.DataFrame(stock_day_rise)

# 添加行索引
# 构造行索引索引序列
stock_code = ['股票' + str(i) for i in range(stock_day_rise.shape[0])]
# 添加行索引
df_row_index = pd.DataFrame(stock_day_rise, index=stock_code)

# 增加列索引
# 生成一个时间的序列，略过周末非交易日
date = pd.date_range('2017-01-01', periods=stock_day_rise.shape[1], freq='B')
# index代表行索引，columns代表列索引
df_columns_index = pd.DataFrame(stock_day_rise, index=stock_code, columns=date)

# 修改行索引
df_columns_index.index = [i for i in range(500)]    # 通过整体修改，不能单个赋值; 如df_columns_index.index[0] = "index0"会报错

# 重置索引
# 当DataFrame或Series类型的数据不是连续的索引，可以使用reset_index()重置索引
df_columns_index.reset_index(drop=True)

# 为某列设置新的索引
df = pd.DataFrame({'month':[1,4,7,10], 'year':[1, 1, 2, 2], 'sale':[55, 40, 84, 31]})
# df.set_index(['month'])# 设置新的索引值，但是返回一个新的dataframe
df = df.set_index(['month'])
# 设置多重索引 MultiIndex的结构
df = df.set_index(['year', df.index])


# 创建series
series = pd.Series(np.arange(10))
# 指定索引
series = pd.Series(np.arange(10), index=["series%s" % i for i in range(10)])
# 通过字典创建Series
series = pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})
# Series获取属性、获取值
series.index
series.values

# 读取csv文件
data = pd.read_csv("../data/stock_day.csv")

# 索引操作
'''
pandas的DataFrame的获取有三种形式：
    1、直接使用行列索引(先列后行)
    2、结合loc或者iloc使用索引
    3、使用ix组合索引(pandas的1.0.0版本开始，移除了Series.ix and DataFrame.ix 方法)
'''
# 通过行列索引
data['open']['2018-02-27']
# loc:只能指定行列索引的名字
data.loc['2018-02-27':'2018-02-22', 'open']
# 使用iloc可以通过索引的下标去获取
data.iloc[0:100, 0:2]
# 使用ix进行下表和名称组合做引
data.ix[0:10, ['open', 'close']]
# 相当于
data[['open', 'close']][0:10]
# ps: 不支持通过索引修改指定的值


# 排序
# 按照涨跌幅大小进行排序。使用ascending指定按照大小排序，默认True升序
df_sort_data = data.sort_values(by='p_change', ascending=False)
# 按照多个键进行排序
df_sort_data = data.sort_values(by=['open', 'high'])
# 对索引进行排序，ascending默认值True升序
df_sort_data = data.sort_index(ascending=False)


# 统计分析
# describe()函数可以查看数据的基本情况，包括：count 非空值数、mean 平均值、std 标准差、max 最大值、min 最小值、（25%、50%、75%）分位数等
data.describe()
# 多列多行统计
df_sum = data.sum()     # 默认max(0)，对列统计
# 对所有列进行统计
df_max = data.max(0)
# 对所有行进行统计
df_min = data.max(1)

# 单行单列统计
# 单列统计
data['close'].max()
# 单行统计
data.loc['2018-02-27'].max()

# 求出最大值的位置。axis默认值0表示一列中最大值对应的位置，反之
col_row = data.idxmax(axis=0)
row_col = data.idxmax(axis=1)

# example:
# 对df某列按行索引排序
# 取指定一列，进行累加求和(第二项为前两项之和，第三项为前三项之和，...）
# 绘图
data_sort = data.sort_index()
stock_rise = data['p_change']
p_change_cumsum = stock_rise.cumsum()
import matplotlib.pyplot as plt
p_change_cumsum.plot()
plt.show()


# 逻辑与算数运算
# 进行逻辑判断，结果用true false进行标记，逻辑判断的结果可以作为筛选的依据
data[data['p_change'] > 2]
# 复合逻辑判断， p_change > 2 且 open > 15
data[(data['p_change'] > 2) & (data['open'] > 15)]
# 可以指定值进行一个判断，从而进行筛选操作
data[data['turnover'].isin([4.19])]
data.head(10)   # 最大显示10行


# 数学运算 加上指定值
data['open'].add(1)


# example：计算两列的差值，并且对应保存一列
close = data['close']
open1 = data['open']
m_price_change = data['m_price_change'] = close.sub(open1)


# 自定义运算函数 apply()
# 求一列中最大值与最小值的差值
data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)
# 求一行中最大值与最小值的差值
data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=1)




