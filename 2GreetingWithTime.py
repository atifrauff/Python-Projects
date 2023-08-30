# First we've to import only time. 'datetime' is not required
import time
# store time in any variable. Right now we're storing it in 'now' variable
now = time.strftime("%I:%M %p")
# printing welcome
print("Welcome to GreetingWithTime v2.0.")
# storing only hour in 'hour' variable
hour = time.strftime("%H")
# casting given hour in integer because by default it gives in value in string
Hour = int(hour)
# use if else statements for greetings according to time
if 4<=Hour<12:
    print("Good Morning, Sir! It's",now,"now.")
elif 12<=Hour<17:
    print("Good Afternoon, Sir! It's",now,"now.")
elif 17<=Hour<20:
    print("Good Evening, Sir! It's",now,"now.")
elif 20<=Hour<24:
    print("Good Night, Sir! It's",now,"now.")
else:
    print("What the hell are you doing here right now? It's",now,"now.")
