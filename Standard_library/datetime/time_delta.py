from datetime import timedelta,datetime
# now when we subtract these two dates we get a timedelta object
dt1 = datetime(50,1,1)
dt2 = datetime.now()
# duration = dt1 - dt2
duration = dt2 - dt1
print(duration)
print(duration.days)

dt1 = datetime(2023,1,1) + timedelta(days=1, seconds=1000)
print(dt1)