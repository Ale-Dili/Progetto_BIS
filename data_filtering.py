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
log = pm4py.convert_to_dataframe(log)
print(log.iloc[0])