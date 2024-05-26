import pm4py
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pickle

#load the log from the pickle file
log = None
with open("data/log_pm4py.pkl", "rb") as f:
    log = pickle.load(f)
log_df = pm4py.convert_to_dataframe(log)
print(log.iloc[0])

log_df.rename(columns={'Case ID': 'case:concept:name', 'Complete Timestamp': 'time:timestamp', 'Activity': 'concept:name', 'Resource': 'org:resource'}, inplace=True) #change the name to a colum
#log_df['time:timestamp']= pd.to_datetime(log_df['time:timestamp'])

num_events = len(log_df)
num_cases = len(log_df['case:concept:name'].unique())
#print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))

start_activities = pm4py.get_start_activities(log_df)
end_activities = pm4py.get_end_activities(log_df)
#print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

#print distribution of duration of cases
case_durations = pm4py.get_all_case_durations(log_df)
#case_durations = case_durations.dropna() #drop rows with NaN values
#case_durations = case_durations[case_durations > datetime.timedelta(0)] #drop rows with negative values
#case_durations = case_durations.apply(lambda x: x.total_seconds()/3600) #convert to hours
#case_durations.hist(bins=50)
plt.xlabel('Duration (hours)')
plt.ylabel('Frequency')
plt.title('Distribution of case durations')
plt.show()
