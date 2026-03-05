import pandas as pd
import pyodbc
print(pyodbc.drivers())
from sqlalchemy import create_engine

# 从本地MySQL读取数据
mysql_engine = create_engine('mysql+pymysql://root:li19980616@localhost/covid19')
df = pd.read_sql('SELECT * FROM compact', mysql_engine)
print(f"从MySQL读取：{len(df)}行")

# 连接Azure SQL
server = 'chelsea-server.database.windows.net'
database = 'covid-db'
username = 'chelsea'
password = 'Li19980616!'

azure_engine = create_engine(
    f'mssql+pyodbc://{username}:{password}@{server}/{database}'
    f'?driver=ODBC+Driver+18+for+SQL+Server'
)

# 写入Azure SQL
df.to_sql('compact', azure_engine, if_exists='replace', index=False)
print("迁移成功")
