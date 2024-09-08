import sqlite3

def create_table():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,
                    humidity REAL,
                    wind_speed REAL,
                    timestamp INTEGER)''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO weather (temperature, humidity, wind_speed, timestamp)
                 VALUES (?, ?, ?, ?)''', (data['temperature'], data['humidity'], data['wind_speed'], data['timestamp']))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
