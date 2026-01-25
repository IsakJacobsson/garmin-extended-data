import pandas as pd
from filters import *
from plotting_functions import *
from summing_functions import *

file_name = 'Activities-25-05-04.csv'
activities = pd.read_csv(file_name)
running_activities = filter_activity(activities, 'Löpning')
attempts_10k = filter_distance(running_activities, min_distance=21, max_distance=23)
attempts_10k_sorted = attempts_10k.sort_values(by='Total tid', ascending=True)

print(attempts_10k_sorted)