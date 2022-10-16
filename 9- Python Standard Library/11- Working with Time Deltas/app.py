from datetime import datetime, timedelta


dt1 = datetime(2020, 2, 2) + timedelta(days=12)
dt2 = datetime.now()

print(dt1)
print(dt2)

dur = dt2 - dt1
print(dur.seconds)
print(dur.days)
print(dur.total_seconds())
