import pandas as pd
import sqlite3

df=pd.read_csv('compact.csv')
cols_needed = [
    'continent', 'country', 'date', 'population',
    'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
    'people_vaccinated_per_hundred'
]
df_raw = df[cols_needed].copy()

#建立SQL数据库
conn = sqlite3.connect('covid.db')
df_raw.to_sql('covid_raw', conn, if_exists='replace', index=False)
print("数据已存入SQLite")

query = """
SELECT 
    continent,
    country,
    date,
    population,
    total_cases,
    new_cases,
    total_deaths,
    new_deaths,
    ROUND((total_deaths * 1.0 / total_cases) * 100, 2) AS death_rate,
    people_vaccinated_per_hundred
FROM covid_raw
WHERE 
    continent IS NOT NULL
    AND total_cases IS NOT NULL
ORDER BY country, date
"""
df_clean = pd.read_sql(query, conn)
conn.close()

print(f"总行数: {len(df_clean)}")
print(df_clean.head())

df_clean.to_csv('covid_clean.csv', index=False)
print("导出成功")