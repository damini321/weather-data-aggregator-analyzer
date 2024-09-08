# Weather Data Aggregator and Analyzer

## Overview
This project fetches weather data from a public API, stores it in a SQLite database, performs basic statistical analysis, and visualizes the data.

## Setup

1. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install dependencies:**
    ```bash
    pip install requests pandas matplotlib seaborn
    ```

   *(Note: `sqlite3` is included with Python's standard library, so you don't need to install it separately.)*

3. **Get an API key from OpenWeatherMap and update `fetch_data.py` with your API key.**

4. **Run the data fetching script:**
    ```bash
    python fetch_data.py
    ```

5. **Analyze the data:**
    ```bash
    python analyze_data.py
    ```

6. **Visualize the data:**
    ```bash
    python visualize_data.py
    ```

## Files
- `fetch_data.py`: Fetches weather data from the API and stores it in the SQLite database.
- `database.py`: Handles SQLite database operations, including table creation and data insertion.
- `analyze_data.py`: Performs basic statistical analysis on the data from the SQLite database.
- `visualize_data.py`: Generates visualizations of the weather data using Matplotlib and Seaborn.
- `README.md`: Documentation for setup and usage.

## Example Outputs
- **Fetched Data:**
  ```json
  {
      "temperature": 293.25,
      "humidity": 75,
      "wind_speed": 3.6,
      "timestamp": 1694150400
  }
- **Analysis Results:**
    ```
    {
        Average Temperature: 294.15
        Average Humidity: 78.0
    }
- **Visualizations:**
    Temperature Over Time
    Humidity Over Time
    Wind Speed Over Time

License
This project is licensed under the MIT License - see the LICENSE file for details.
