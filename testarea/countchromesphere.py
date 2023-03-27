import pandas as pd

# 读取数据，指定空格为分隔符，没有列名
df = pd.read_csv('./result_log.txt', sep=' ', header=None)

value_counts = df.iloc[:, 9].value_counts()

print(value_counts)
