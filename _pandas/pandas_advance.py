import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 读取csv数据
movie = pd.read_csv("../data/IMDB-Movie-Data.csv")
print(movie)

# 删除np.nan缺失值
movie.dropna()
# 当缺失值是np.nan，fillna()直接替换
movie['Metascore'].fillna(movie['Metascore'].mean(), inplace=True)

# 不是缺失值nan，有默认标记的
# 先将特殊字符替换成np.nan，再对np.nan缺失值进行处理
'''
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1051)>
# SSL 证书的验证问题。添加以下两行代码：
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
wis = wis.replace(to_replace='?', value=np.nan) # 把'?'字符替换为np.nan
wis.dropna()


# 验证涨跌幅变化是否符合正态分布
data = pd.read_csv("../data/stock_day.csv")
p_change= data['p_change']
p_change.hist(bins=80)  # hist()绘制数据分布直方图。bins指bin(箱子)的个数，即每张图柱子的个数
plt.show()


# 将股票涨跌幅数据进行分组
# 自行分组
qcut = pd.qcut(np.abs(p_change), 10)
qcut.value_counts()     # 统计每组个数
# 自定义区间分组
bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
p_counts = pd.cut(p_change, bins)
p_counts.value_counts()


# 股票涨跌幅分组数据变成哑变量矩阵
dummaries = pd.get_dummies(p_counts, prefix="rise")

# 如我们将刚才处理好的哑变量与原数据合并
pd.concat([data, dummaries], axis=1)


# 案例分析：
# 一、准备两列数据，星期数据以及涨跌幅是好是坏数据。进行交叉表计算

# 寻找星期几跟股票张得的关系
# 1、先把对应的日期找到星期几
date = pd.to_datetime(data.index).weekday
data['week'] = date
# 2、假如把p_change按照大小去分个类0为界限
data['posi_neg'] = np.where(data['p_change'] > 0, 1, 0)

# 通过交叉表找寻两列数据的关系
count = pd.crosstab(data['week'], data['posi_neg'])

# 二、对于每个星期一等的总天数求和，运用除法运算求出比例
# 算数运算，先求和
count.sum(axis=1).astype(np.float32)
pro = count.div(count.sum(axis=1).astype(np.float32), axis=0)

# 三、使用stacked的柱状图绘图
pro.plot(kind='bar', stacked=True)
plt.show()

# 四、使用pivot_table(透视表)实现上述功能
data.pivot_table(['posi_neg'], index=['week'])



col = pd.DataFrame({'color': ['white','red','green','red','green'], 'object': ['pen','pencil','pencil','ashtray','pen'],'price1':[5.56,4.20,1.30,0.56,2.75],'price2':[4.75,4.12,1.60,0.75,3.15]})
# 分组，并求平均值
col.groupby(['color'])['price1'].mean()
# 等同于以下
col['price1'].groupby(col['color']).mean()
# 分组，数据的结构不变
col.groupby(['color'], as_index=False)['price1'].mean()


# 实例：
# 星巴克零售店面数据
# 数据来源：https://www.kaggle.com/starbucks/store-locations/data
# 1、导入星巴克店的数据
starbucks = pd.read_csv("../data/directory.csv")
# 2、按照国家分组，求出每个国家的星巴克零售店数量
count = starbucks.groupby(['Country']).count()
# 3、绘图
count['Brand'].plot(kind='bar', figsize=(20, 8))
plt.show()