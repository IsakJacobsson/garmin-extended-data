from filters import filter_for_distance

def get_time(df):
  '''Returns the time spent on activities in hours'''

  return round(sum([int(time[:2]) + int(time[3:5]) / 60 + float(time[6:]) / 3600 for time in df['Tid']]),2)

def get_distance(df):
  '''Returns the distance covered in km'''

  df = filter_for_distance(df)
  distances = []
  for value in df['Distans']:
      try:
          distances.append(float(value.replace(',', '.')))
      except ValueError:
          print("hhaall")
  return round(sum(distances), 2)

def max_heart_rate(df):
  '''Returns max heart rate'''

  return max([int(hr) for hr in df['Maxpuls'] if hr.isdigit()])

def avg_heart_rate(df):
  '''Return average heart rate'''

  hr_df = [int(hr) for hr in df['Medelpuls'] if hr.isdigit()]
  if len(hr_df) == 0: return 0
  return sum(hr_df) / len(hr_df)