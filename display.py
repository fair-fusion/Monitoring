import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv', names=['datetime', 'temperature', 'humidity'])

# Convert the datetime column to a datetime object
df['datetime'] = pd.to_datetime(df['datetime'])

# Create new columns for date, time, month, year, and week number
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year
df['week'] = df['datetime'].dt.week

# Create the graph
plt.plot(df['datetime'], df['temperature'])
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over Time')
plt.show()