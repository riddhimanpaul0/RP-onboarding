"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


sampleData = pd.read_csv(r'C:\Users\riddh\OneDrive\Projects\MidnightSunOnboard\strategy-onboarding\task2_coding_exercises\q3_test_data.csv', header=None)

arr1 = np.array(sampleData.iloc[:, 1])
arr2 = np.array(sampleData.iloc[:, 2])
arr3 = np.array(sampleData.iloc[:, 3])
arr4 = np.array(sampleData.iloc[:, 4])

arr0 = np.array(sampleData.iloc[:, 0])

plt.plot(arr0, arr1)
plt.plot(arr0, arr2)
plt.plot(arr0, arr3)
plt.plot(arr0, arr4)

plt.show()