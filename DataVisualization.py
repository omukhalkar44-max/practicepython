import pandas as pd
import numpprac as np 
import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
monthly = [100, 150, 200, 250, 300, 350, 50]
year = [1200, 1800, 2400, 3000, 3600, 4200, 600]
plt.bar(days, monthly, color='red')


print("Bar chart created successfully.")

plt.title("Bar chart of monthly data")
plt.ylabel("Monthly Data")
plt.xlabel("Days ")
plt.show()


