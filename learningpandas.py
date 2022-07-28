import pandas as pd

url = "./tips.csv"
tips = pd.read_csv(url)
print(tips)
