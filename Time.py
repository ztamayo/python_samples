# Programmer: Zailyn Tamayo

# This script will read the time and output it.  
# For example, if it is 2:30pm, the output will read "Two".  
# It will only grab the hour and not the minutes.

from time import strftime

# Get date and time in Hours format
dt = strftime("%H")

if (int(dt) > 12):
  dt = int(dt) - 12;

if dt == 0:
  print ("Zero")

elif dt == 1:
  print ("One")

elif dt == 2:
  print ("Two")

elif dt == 3:
  print ("Three")

elif dt == 4:
  print ("Four")

elif dt == 5:
  print ("Five")

elif dt == 6:
  print ("Six")

elif dt == 7:
  print ("Seven")

elif dt == 8:
  print ("Eight")

elif dt == 9:
  print ("Nine")

elif dt == 10:
  print ("Ten")

else:
  print ("Eleven")
