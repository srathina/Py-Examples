import datetime

print(datetime.date(2020,7,7))
print(datetime.time(10,10,10))
print(datetime.datetime(2000,7,7,10,10,10))

now = datetime.datetime.today()
print(now)
print(now.microsecond)

date = datetime.datetime(2020,7,7,10,10,10)+datetime.timedelta(365)
print(date.strftime("%A"))

exam_date = "2/5/2020"
print(f'Exam date: { datetime.datetime.strptime(exam_date,"%m/%d/%Y")}')
