import datetime
start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '20:30', '%Y-%m-%d%H:%M')
end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '21:00', '%Y-%m-%d%H:%M')
now_time = datetime.datetime.now()


print(start_time)
print(end_time)
print(now_time)

print(start_time<now_time<end_time)