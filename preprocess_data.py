import numpprac as np
import pandas as pd

data = {
        'Name': ['Ashu', 'yash', 'jay', 'vedant'],
        'Age': [25, 30, 35, 40],
        'City': ['akola', 'amravati', 'nagpur', 'pune'] 
    }  
dataframe = pd.DataFrame(data)
show_dataframe = dataframe.head()
pd.DataFrame = show_dataframe
print("DataFrame:")
print(dataframe)