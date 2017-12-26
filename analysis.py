import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir("C:\\Users\\Callum\\Dropbox\\code\\Polar-H7-Pi")

names = [f for f in os.listdir() if f[-4:] == ".csv"]

df = pd.concat(pd.read_csv(name, names=["HR", "Time"]) for name in names)

df["Time"] = pd.to_datetime("26/12/2017 " + df["Time"],
                            infer_datetime_format=True)
plt.plot(df["Time"], df["HR"])
