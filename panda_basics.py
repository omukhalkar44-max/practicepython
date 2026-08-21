import pandas as pd

marks = pd.Series([85, 72, 91, 68])

print(marks)

marks2 = pd.Series([85, 72, 91, 68])
marks3 = pd.Index([1, 2, 3, 4])
print(marks2,marks3)

data = {'Name': ['om ',
                  'ashish', 
                  'jayyy', 
                  'yashhhhhhh'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'amt']}
print(data)