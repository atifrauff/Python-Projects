print("Welcome to Our Namaz timer v1.0!")
import time
timeNow = time.strftime("%I:%M %p")
print("It's",timeNow,"right now.")
hourNow = time.strftime("%H")
hours = int(hourNow)
if 4<=hours<6:
    print("You can offer Fajar prayer now.")
elif 6>=hours>12:
    print("It's not time of any Namaz.")
elif 12<=hours<15:
    print("You can offer Zuhr prayer now.")
elif 15<=hours<19:
    print("You can offer Asar prayer now.")
elif 19<=hours<21:
    print("You can offer Maghrib prayer now.")
elif 21<hours<3:
    print("You can offer Ishaa prayer now.")
