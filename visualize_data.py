import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def plot_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(df['timestamp'], df['temperature'], label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature Over Time')
    
    plt.subplot(3, 1, 2)
    plt.plot(df['timestamp'], df['humidity'], label='Humidity')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Over Time')
    
    plt.subplot(3, 1, 3)
    plt.plot(df['timestamp'], df['wind_speed'], label='Wind Speed')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Wind Speed Over Time')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data()
