# Programmer: Zailyn Tamayo
# Prompts user to enter a number and then outputs the square root of that number.

import string
import math

def getSqrt(n):
  return math.sqrt(float(n))

s = input("\nEnter a numerical value: ")

try:
   for i in s:
      if (i.isdigit() or i == "."):
          sType = "nonstr"

   if (sType == "nonstr"):
       print("\n")
       print(getSqrt(s))

except ValueError as ex:
   print("\nNon numberical value...")


