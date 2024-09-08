import pandas as pd
import sqlite3

def analyze_data():
    conn = sqlite3.connect('weather_data.db')
    query = 'SELECT * FROM weather'
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    print("Average Temperature:", df['temperature'].mean())
    print("Average Humidity:", df['humidity'].mean())

if __name__ == "__main__":
    analyze_data()
