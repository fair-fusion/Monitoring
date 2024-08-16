#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv', names=['date_time', 'temperature', 'humidity'])

# Convert the date_time column to a date_time object
df['date_time'] = pd.to_datetime(df['date_time'])

# Create new columns for date, time, month, year, and week number
df['date'] = df['date_time'].dt.date
df['time'] = df['date_time'].dt.time
df['month'] = df['date_time'].dt.month
df['year'] = df['date_time'].dt.year
df['week'] = df['date_time'].dt.week

# Create the graph using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.lineplot(x="date_time", y="temperature", data=df)
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over Time')
plt.show()

# Create the graph using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.lineplot(x="date_time", y="humidity", data=df)