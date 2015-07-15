#The import statement gives us access to functionality of the datetime class
import datetime
#today is a function that returns todays date
currentDate = datetime.date.today()
currenttime = datetime.datetime.now()
print ("Current time is ", currenttime)
print (currentDate)
print(currentDate.year)
print(currentDate.month)
#strftime (string from time) allows to specify the date format full list strftime.org
print(currentDate.strftime('%d %b %Y'))
print(currentDate.strftime
      ('Please attend our event %a, %b %d in th eyear %Y'))

birthday = input("when is your next birthday ")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
#why did we list datetime twice?
#because we are calling the strptime function which is part of the datetime class
#which is in the datetime module
print(" ur birth month is " + birthdate.strftime('%B'))
difference = birthdate - currentDate
print(difference.days)

#for more function on date go to http:\\labix.org/python-dateutil
#launchpad.net/dateutil





