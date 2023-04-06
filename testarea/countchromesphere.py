import pandas as pd

# 读取数据，指定空格为分隔符，没有列名
df = pd.read_csv('./result_log.txt', sep=' ', header=None)
value_counts = df.iloc[:, 9].value_counts()
print(value_counts)

# 统计DataFrame中的行数，即数据总数
total_count = len(df)
print("Total count:", total_count)
