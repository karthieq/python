import datetime
import pytz

tday = datetime.date.today()
print(tday)

day1 = datetime.timedelta(days=1)
print(tday - day1)

day7 = datetime.timedelta(days=7)
print(tday - day7)

now = datetime.datetime.now()
print(now)
print(now.strftime('%Y-%b-%d %H:%M:%S'))
tday = datetime.datetime.today()
print(tday)
unow = datetime.datetime.utcnow()
print(unow)
print(int(unow.timestamp()))

dt = datetime.datetime.now(tz=pytz.UTC)
print(dt)
print(dt.astimezone(pytz.timezone('Asia/Calcutta')))
# for tz in pytz.all_timezones:
#     print(tz)

dat = '2023-03-29T08:06:00+00:00'
odat = datetime.datetime.strptime(dat, '%Y-%m-%dT%H:%M:%S%z')
print(odat.strftime('%Y-%m-%d %H:%M:%S'))
