import pandas as pd
import numpy as np
#pandas series 
marks = pd.Series([85, 72, 91, 68])

print(marks)

marks2 = pd.Series([85, 72, 91, 68])
marks3 = pd.Index([1, 2, 3, 4])
print(marks2,marks3)
print("=================================")
data = {'Name': ['om ',
                  'ashish', 
                  'jayyy', 
                  'yashhhhhhh'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'amt']}
print(data)

df = pd.DataFrame(data)
total = df['Age'].sum()

print(df)
print("total age",total)

df = pd.DataFrame(data)
find_max_age = df['Age'].max()
print("maxxx age",find_max_age)

df= pd.DataFrame(data)
value_counts = df['Age'].value_counts()
print("value counts",value_counts)

df= pd.DataFrame(data)
upper_case_names = df['Name'].str.upper()

print("upper case name",upper_case_names)

df= pd.DataFrame(data)
replaced_names = df['Name'].str.replace('om', 'kajukatliiiiiiiiiiiiiiiiiiii')
print("replaced names", replaced_names)

#numpy operations
print("--------------------------------")

numpy =np.array([4, 8, 15, 16, 23, 42])
np.sum(numpy)
print("min value",np.sum
      (numpy))