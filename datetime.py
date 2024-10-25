import datetime
print(datetime.datetime.now())
x = datetime.datetime.now()
today = datetime.date.today()
print(x.strftime('%X'))
print(x.strftime('%m'))
print(x.strftime('%d'))
print(x.strftime('%Y'))