# practicepython
# Python Date & Time Program

This is a simple Python program that demonstrates how to use the built-in `datetime` module.

## Features

* Displays the current date and time
* Creates and displays a specific date
* Creates and displays a specific time
* Calculates the difference between two dates
* Displays the difference in days

## Python Concepts Used

* `datetime`
* `date`
* `time`
* Date subtraction
* `timedelta`
* `.days` attribute

## Code

```python
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print("Current date:", now)

# Specific date
d = date(2026, 7, 29)
print("Specific Date:", d)

# Specific time
t = time(4, 45, 25)
print("Current time:", t)

# Date difference
date1 = date(2026, 7, 29)
date2 = date(2026, 8, 15)

difference = date2 - date1

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference:", difference)
print("Difference in Days:", difference.days)
```

## Sample Output

```text
Current date: 2026-08-20 22:45:51.254437
Specific Date: 2026-07-29
Current time: 04:45:25
Date 1: 2026-07-29
Date 2: 2026-08-15
Difference: 17 days, 0:00:00
Difference in Days: 17
```

## How to Run

Open the terminal in the project folder and run:

```bash
python DATE-TIME.py
```

## Repository

This project is created for practicing Python's `datetime` module and basic date/time operations.


#python datavisualizationcode
DataVisualization.py

A simple Python script that demonstrates basic data visualization using pandas, numpy, and matplotlib.

Description

This script creates a bar chart comparing monthly data values across the days of the week using matplotlib.pyplot.

Requirements
Python 3.x
pandas
numpy
matplotlib

Install the dependencies with:

bash
pip install pandas numpy matplotlib
Usage

Run the script from the terminal:

bash
python DataVisualization.py

This will display a bar chart titled "Bar chart of monthly data", with:

X-axis: Days of the week
Y-axis: Monthly data values
Bar color: Red
Sample Output
Bar chart created successfully.

A bar chart window will open showing monthly values plotted against each day of the week.
# practicepython

Daily Python practice scripts.

---

## DataVisualization.py
A simple Python script that demonstrates basic data visualization using pandas, numpy, and matplotlib.

### Description
This script creates a bar chart comparing monthly data values across the days of the week using `matplotlib.pyplot`.

### Requirements
- Python 3.x
- pandas
- numpy
- matplotlib

Install the dependencies with:
```bash
pip install pandas numpy matplotlib
```

### Usage
```bash
python DataVisualization.py
```

This will display a bar chart titled "Bar chart of monthly data", with:
- X-axis: Days of the week
- Y-axis: Monthly data values
- Bar color: Red

### Sample Output
