import pandas as pd
import matplotlib.pyplot as plt
from filters import filter_for_distance
from summing_functions import get_time, get_distance, max_heart_rate, avg_heart_rate

def plot_nbr_activities(df_original):
  '''Plots the number of activities over time'''

  df = df_original.copy()

  df['Datum'] = pd.to_datetime(df['Datum'])

  df['Datum'] = df['Datum'].dt.date

  activity_count = df.groupby('Datum')['Aktivitetstyp'].count().cumsum()

  plot(activity_count, 'Number of Activities Over Time', 'Date', 'Number of Activities')

def plot_distance(df_original):
  '''Plots the distance over time'''

  df = df_original.copy()

  df = filter_for_distance(df)

  df['Datum'] = pd.to_datetime(df['Datum'])

  df['Datum'] = df['Datum'].dt.date

  activity_count = df.groupby('Datum')['Aktivitetstyp'].count().cumsum()

  plot(activity_count, 'Distance Over Time', 'Date', 'Distance (km)')

def plot(activity_count, title, xlabel, ylabel, figsize=(8, 5), marker='.', color='b', grid=True):
  '''Plots the activity count'''

  plt.figure(figsize=figsize)
  plt.scatter(activity_count.index, activity_count.values, marker=marker, color=color)
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid(grid)
  plt.show()

def print_summary(df):
  '''Prints time, distance and number of sessions'''

  print(f"Time: {get_time(df)} hours")
  print(f"Distance: {get_distance(df)} km")
  print(f"Sessions: {len(df)}")
  print(f"Average heart rate: {avg_heart_rate(df)} bpm")
  print(f"Max heart rate: {max_heart_rate(df)} bpm")