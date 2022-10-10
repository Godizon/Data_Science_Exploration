import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

df.plot(x = 'Duration', y = 'Calories') #for taking values from x and y
plt.xticks(np.arange(40, 100, 5))
plt.yticks(np.arange(300, 500, 50))
plt.title('data analysis')
plt.xlabel('duration')
plt.ylabel('calories')
plt.show()

# This code prints a graph with Duration on X axis and Calories on Y axis and plots the relation between them.
