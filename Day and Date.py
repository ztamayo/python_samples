# Programmer: Zailyn Tamayo; Date: 04/26/2013

# Prints out the day of the week and date.  
# For example, Tuesday, June 6th, 2017.

import time

import datetime

# get the current date

t = datetime.date.today()

Y = t.strftime("%Y"); # current 4-digit year

m = t.strftime("%m"); # current month

d = t.strftime("%d"); # day of month

w = t.strftime("%w"); # day of week

# use list to create an array for month

month = ["January", "February", "March", "April",
         "May", "June", "July", "August", "September",
         "October", "November", "December" ]

# use tuple to create an array for days

day = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th",
       "8th", "9th", "10th", "11th", "12th", "13th",
       "14th", "15th", "16th", "17th", "18th", "19th",
       "20th", "21st", "22nd", "23rd", "24th", "25th",
       "26th", "27th", "28th", "29th", "30th", "31st" )

# use dictionary to create an associate array for weekdays

week = {"0": "Sunday", "1": "Monday", "2": "Tuesday",
        "3": "Wednesday", "4": "Thursday", "5": "Friday",
        "6": "Saturday" };

# int() does type cast

print ("\nToday is", week[w], "the", day[int(d)-1], "day of", month[int(m)-1], ",",Y);
