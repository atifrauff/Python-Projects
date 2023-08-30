# This is experimental
import datetime
currentTime = datetime.datetime.now()
hour = int(currentTime.strftime("%H"))
print("The current time is,", currentTime)
if hour<12:
    print("Good Morning, Sir!")
elif 18>hour>12:
    print("Good Afternoon, Sir!")
elif 18<hour<20:
    print("Good Evening, Sir!")
else:
    print("Good Night, Sir!")
