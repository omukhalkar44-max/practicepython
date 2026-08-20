from datetime import datetime, date, time
#current time 
now = datetime.now()
print ("current date :",now)
# current_time 

#date
d = date(2026, 7, 29)
print("Specific Date:", d)


#time specific 
t = time(4,45,25)
print("crrent time",t)


#date diff

date1 = date(2026, 7, 29)
date2 = date(2026, 8, 15)


difference = date2 - date1


print("Date 1:", date1)
print("Date 2:", date2)
print("Difference:", difference)
print("Difference in Days:", difference.days)