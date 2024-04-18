import datetime
today_date = datetime.date.today()
current_time = datetime.datetime.now().time()
today_day = today_date.strftime("%A")
print("Today's date:",today_date)
print("Current Time:",current_time)
print("today's Day:",today_day)
