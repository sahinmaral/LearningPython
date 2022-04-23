from datetime import datetime

simdi = datetime.now()
simdi_year = simdi.year
simdi_day = simdi.day
simdi_month = simdi.month
simdi_hour = simdi.hour
simdi_minute = simdi.minute

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y %B %A')

string_date = '21 Nisan 2019'
gun , ay , yil = string_date.split()
# print(gun,ay,yil)

string_date2 = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(string_date2,'%d %B %Y hour %H:%M:%S')

# print(dt)

birthday = datetime(1983,5,9,12,30,10)
result = datetime.timestamp(birthday) # Saniye cinsine donusturur

result = datetime.fromtimestamp(0) # 1970-01-01

result = simdi - birthday # timedelta

# result = result.days
result = result.seconds

print(result)