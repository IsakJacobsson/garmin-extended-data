def filter_for_distance(df):
  '''Removes all activities that are not distance based'''
  
  exclude = ['Simbassäng', 'Konditionspass', 'Styrketräning', 'Yoga']
  filter = ~df['Aktivitetstyp'].isin(exclude)
  df = df[filter]
  return df

def filter_distance(df, min_distance=None, max_distance=None):
  '''Filters activities with distance between range min and max'''

  distance_df = filter_for_distance(df).copy()
  distance_df['Distans'] = distance_df['Distans'].astype(float)
  if min_distance is not None:
    distance_df = distance_df[distance_df['Distans'] >= min_distance]
  if max_distance is not None:
    distance_df = distance_df[distance_df['Distans'] <= max_distance]
  
  distance_df["Distans"] = distance_df["Distans"].astype(str)

  return distance_df


def filter_time(df, start=None, end=None):
  '''Filters activities based on time'''
  
  if start is not None:
    filter = df['Datum'] >= start
    df = df[filter]
  if end is not None:
    filter = df['Datum'] <= end
    df = df[filter]

  return df

def filter_activity(df, activity):
  '''Filters activities based on activity type'''

  filter = df['Aktivitetstyp'] == activity
  df = df[filter]
  return df

def filter_name(df, name):
  '''Filters activities that contain a string'''

  filter = df['Namn'].str.contains(name, case=False)
  df = df[filter]
  return df
