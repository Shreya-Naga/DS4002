import pandas as pd

#read the csv file
df = pd.read_csv('cdc_npao.csv')
print(list(df.columns))

#delete unnecessary columns
df_clean = df.drop('low_confidence_limit', axis='columns')

print(list(df_clean.columns))