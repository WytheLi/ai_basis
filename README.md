### Jupyter使用
```
# 启动jupyter
jupyter notebook
```


### Pandas
1、Pandas数据结构

1.1 Pandas有三大数据结构，Series、DataFrame以及Panel
- Series(一维数据)
- DataFrame(二维数据)
- Panel(三维结构数据/面板数据)

1.2 DatatFrame的属性
- shape
- dtypes
- ndim
- index
- columns
- values
- T

还有一些方便整体查询的属性
- head(5)
- tail(5)

2、统计分析函数

2.1 基本统计分析函数

|count	|Number of non-NA observations  |
|----   |----   |
|sum	|Sum of values|
|mean	|Mean of values|
|mad	|Mean absolute deviation|
|median	|Arithmetic median of values|
|min	|Minimum|
|max	|Maximum|
|mode	|Mode|
|abs	|Absolute Value|
|prod	|Product of values|
|std	|Bessel-corrected sample standard deviation|
|var	|Unbiased variance|
|idxmax	|compute the index labels with the maximum|
|idxmin	|compute the index labels with the minimum|

2.2 累计统计分析函数

|函数	|作用 |
|----   |----|
|cumsum	|计算前1/2/3/…/n个数的和|
|cummax	|计算前1/2/3/…/n个数的最大值|
|cummin	|计算前1/2/3/…/n个数的最小值|
|cumprod|计算前1/2/3/…/n个数的积|


3、文件读取与存储

pandas的API支持众多的文件格式，如CSV、SQL、XLS、JSON、HDF5

![](material/img/readh5.png)
需要安装安装tables模块避免不能读取hdf文件
```
pip install tables
```

4、数据复杂处理

4.1 缺失值处理

4.2 数据离散化

4.3 合并

4.4 交叉表和透视表

4.5 分组与聚合
