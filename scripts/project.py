import pandas as pd
import sqlite3

# 1. CSV load karo aur missing values clean karo
df = pd.read_csv('vgsales.csv')
df = df.dropna(subset=['Year', 'Publisher'])

# 2. Local SQLite database connection banao
conn = sqlite3.connect('vgsales.db')

# 3. DataFrame ko SQL table mein convert kar do (Table ka naam: video_games)
df.to_sql('video_games', conn, if_exists='replace', index=False)

print("Database successfully ban gaya aur data SQL table mein load ho gaya!")
conn.close()

import sqlite3

# Database se connection jodo
conn = sqlite3.connect('vgsales.db')
cursor = conn.cursor()

print("--- STEP 2: RUNNING ADVANCED SQL ANALYTICS ---")

# 1. Top 5 Publishers with highest total Global Sales
print("\n1. Top 5 Publishers by Total Global Sales:")
query_top_publishers = """
    SELECT Publisher, ROUND(SUM(Global_Sales), 2) AS Total_Sales
    FROM video_games
    GROUP BY Publisher
    ORDER BY Total_Sales DESC
    LIMIT 5;
"""
for row in cursor.execute(query_top_publishers):
    print(f"Publisher: {row[0]} | Total Sales (Millions): {row[1]}")

# 2. Yearly Gaming Trend (Total games released & sales per year)
print("\n2. Yearly Sales Trend (Last 5 Years in dataset):")
query_yearly = """
    SELECT Year, COUNT(Name) AS Games_Released, ROUND(SUM(Global_Sales), 2) AS Total_Sales
    FROM video_games
    WHERE Year IS NOT NULL
    GROUP BY Year
    ORDER BY Year DESC
    LIMIT 5;
"""
for row in cursor.execute(query_yearly):
    print(f"Year: {int(row[0])} | Games Released: {row[1]} | Sales: {row[2]}")

# Connection close karo
conn.close()