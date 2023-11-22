#!/usr/bin/env python
# coding: utf-8

# # <center>AI Lab 11</center> 
# ## <center>Roll Number: </center> 
# **Total marks**: 50 

# Read the last two lines of any text file

# In[1]:


with open('your_file.txt', 'r') as file:
    lines = file.readlines()
    last_two_lines = lines[-2:]
    print(last_two_lines)



# Create a dictionary of student **Ali** where the keys are courses and values are total and obtaining marks in each course. Save this dictionary in a text file and numpy file. 

# In[ ]:


import numpy as np

# Create the dictionary
ali_data = {'PF': {'total': 100, 'obtained': 70},
            'DL': {'total': 90, 'obtained': 60},
            'CV': {'total': 50, 'obtained': 40}}

# Save to text file
with open('ali_data.txt', 'w') as file:
    for course, data in ali_data.items():
        file.write(f"{course}: {data['total']} {data['obtained']}\n")

# Save to numpy file
np.save('ali_data.npy', ali_data)



# Reproduce this bar graph. 

# In[ ]:


courses = ['PF', 'DL', 'CV']
y_pos = [2, 0, 1] 
scores = [70, 60, 40]

import matplotlib.pyplot as plt

courses = ['PF', 'DL', 'CV']
y_pos = [2, 0, 1]
scores = [70, 60, 40]

plt.barh(y_pos, scores, align='center', alpha=0.7)
plt.yticks(y_pos, courses)
plt.xlabel('Scores')
plt.title('Student Ali - Course Scores')
plt.show()



# Reproduce this figure.  **(4 marks)**

# In[ ]:


x = np.arange(0,4*np.pi-1,0.1)  
sin_curve = np.sin(x)
cos_curve = np.cos(x)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi - 1, 0.1)
sin_curve = np.sin(x)
cos_curve = np.cos(x)

plt.plot(x, sin_curve, label='sin(x)')
plt.plot(x, cos_curve, label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Curves')
plt.show()



# Reproduce this figure.  

# In[ ]:


# from numpy.polynomial.polynomial import polyfit
# noise = np.random.uniform(-20, 20, 100)
# x = np.linspace(0, 100, 100)+noise
# y = np.linspace(0, 50, 100)+noise
# plt.scatter( # add code here)
# b, m = polyfit(x, y, 1)
# y_pred = m*x+b
# plt.plot(# add code here)



import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

noise = np.random.uniform(-20, 20, 100)
x = np.linspace(0, 100, 100) + noise
y = np.linspace(0, 50, 100) + noise

plt.scatter(x, y, label='Data Points')
b, m = polyfit(x, y, 1)
y_pred = m * x + b
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Regression Line')
plt.show()





# Download iris flower dataset from kaggle (https://www.kaggle.com/datasets/arshid/iris-flower-dataset) and read it in python dataframe

# In[ ]:


import pandas as pd


iris_df = pd.read_csv('iris.csv')

# Display the first few rows of the DataFrame
print(iris_df.head())



# Do all the preprocessing on the dataset and visulize the data step by step

# In[ ]:

# Example preprocessing steps
# Replace 'your_column' with the actual column name in your dataset
iris_df['sepal_length'] = iris_df['sepal_length'].fillna(0)

# Visualization
# Replace 'your_column_1' and 'your_column_2' with actual column names
plt.scatter(iris_df['sepal_width'], iris_df['petal_length'])
plt.xlabel('sepal_width')
plt.ylabel('petal_length')
plt.title('Scatter Plot of Iris Dataset')
plt.show()



