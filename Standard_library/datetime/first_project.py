from datetime import datetime
import time
dt = datetime(2023,7,24)

print(dt.now())
dt = datetime.strptime("2023/01/01", "%Y/%m/%d")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(dt)

print(f'{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}.{dt.second}.{dt.microsecond}')