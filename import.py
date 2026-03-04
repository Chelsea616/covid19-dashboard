import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('compact.csv')



df_clean = df.copy()
df_clean['date'] = pd.to_datetime(df_clean['date'])

print(f"总行数: {len(df_clean)}")
print(f"国家数量: {df_clean['country'].nunique()}")

engine = create_engine('mysql+pymysql://root:li19980616@localhost/covid19')
df_clean.to_sql('compact', con=engine, if_exists='replace', index=False)
print("导入成功")