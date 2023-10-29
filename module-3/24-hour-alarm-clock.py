'''
Code prompt:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem. Ask the user
for the time now (in hours) and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on a 24-hour clock when the alarm goes
off.
'''

#Set the number of hours in a day, which will be used with the modulo function to
#determine the time of the alarm
hours_in_a_day = 24

#Gather the current time in hours
print('Enter time now (in hours): ', end = '')
time_now = int(input())

#Gather the number of hour to wait until the alarm goes off 
print('How many hours until alarm goes off (in hours)?: ', end = '')
hours_until_alarm = int(input())

#Using the modulo function, determine the number of hours from now until the alarm goes
#off and output that value to the user
alarm_time = (time_now + hours_until_alarm) % hours_in_a_day
print('\nAlarm will go off at the', alarm_time, 'hour', end = '')

#Extra newline printed out to make the code easier to read
print()