import datetime
import pytz

tday = datetime.date.today()
print(tday) # prints the current date in YYYY-MM-DD format
# print(tday.weekday()) # prints number between 0 and 6 with Monday being 0
# tdelta = datetime.timedelta(days=7)
# # print(tday + tdelta) # prints the date 7 days in the future 
# bday = datetime.date(2021, 7, 2)
# # print(bday) # prints my bday in 2021
# till_bday = abs(tday - bday) # days until my bday in 2021
# # print(till_bday.total_seconds()) # seconds until my next bday
# # print(till_bday.days) # days until my next bday

# t = datetime.time(9, 30, 45, 100000) # creates an object of the class time with format HH:MM:SS.microseconds
# # print(t)
# # print(t.hour) # prints only hour

# dt = datetime.datetime(2020, 7, 22, 12, 30, 45, 100000)
# dt1 = datetime.datetime.now()
# print(dt1)

# tdeltad = datetime.timedelta(days = 7) # creates a timedelta in days
# tdeltah = datetime.timedelta(hours = 8) # creates a timedelta in hours
# print(dt1 + tdeltah)

# dt_today = datetime.datetime.today() # gives the current time in the local timezone
# dt_now = datetime.datetime.now() # gives the current time but allows you to specify other timezone. If tz not specified, then same as above.
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2020, 7, 22, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz = pytz.UTC)  # provides the current date time with UTC stored in the dt
# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain')) # dt of central timezone for current time
# print(dt_mtn)

# dt_cen = datetime.datetime.now()
# print(dt_cen)
# cen_tz = pytz.timezone('US/Central')
# dt_cen = cen_tz.localize(dt_cen)
# print(dt_cen)

# dt_east = dt_cen.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# print(dt_cen.isoformat()) # isoformat, the international standard for datetime

# #strftime - Datetime to string
# print(dt_cen.strftime('%A %B %d, %Y at %I:%M%p'))

# #strptime - string to datetime
# dt_str = 'Wednesday July 22, 2020 at 09:57PM'
# dt = datetime.datetime.strptime(dt_str, '%A %B %d, %Y at %I:%M%p')
# print(dt)

# for tz in pytz.all_timezones:
#     print(tz) # prints all timezones available












# def add_time(start, duration, **kwargs):
#     dt = datetime.datetime.strptime(start, '%I:%M %p')
#     print(dt)
#     tdeltalist = duration.split(':')
#     hdelta = int(tdeltalist[0])
#     mdelta = int(tdeltalist[1])
#     tdelta = datetime.timedelta(hours = hdelta, minutes = mdelta)
#     new_time = dt + tdelta
#     print(new_time)
#     new_time = new_time.strftime('%I:%M %p')
#     if 



#     return new_time