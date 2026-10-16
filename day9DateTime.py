import datetime

current_time=datetime.datetime.now()

print("Current date and time:",current_time)
print("formatted Date:",current_time.strftime("%d-%m-%Y"))
print("Formatted Time:",current_time.strftime("%H:%M:%S"))

day_number=current_time.weekday()
print("Weekday number:",day_number)


#o/p
'''
Current date and time: 2026-10-16 14:36:44.946648
formatted Date: 16-10-2026
Formatted Time: 14:36:44
Weekday number: 4
'''