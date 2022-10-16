# import datetime

# dt = datetime.datetime(1987, 1, 22)

# print(dt)

import time
from datetime import datetime
dt1 = datetime(1987, 1, 22)
print(dt1)

dt2 = datetime.now()
print(dt2)

# dt = datetime.strftime()
dt = datetime.strptime("22.01.1987", "%d.%m.%Y")
print(dt)


dt = datetime.fromtimestamp(time.time())
print(f"{dt.day}.{dt.month}.{dt.year}")
print(dt.strftime("%d.%m.%Y"))

print(dt1 > dt2)
