import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("C:\\Users\\Callum\\Dropbox\\code\\Polar-H7-Pi")

names = ["11-09-37.237962.csv", "11-11-18.485575.csv", "11-12-58.732744.csv",
         "11-14-40.477777.csv"]
print(os.getcwd())

df = pd.concat(pd.read_csv(name, names=["HR", "Time"]) for name in names)



df["Time"] = pd.to_datetime("26/12/2017 " + df["Time"],
                            infer_datetime_format=True)
plt.plot(df["Time"], df["HR"])
