import pm4py
import pickle

log_pm4py = pm4py.read_xes("data/Road_Traffic_Fine_Management_Process.xes")

# Save the log to a pickle file
with open("data/log_pm4py.pkl", "wb") as f:
    pickle.dump(log_pm4py, f)