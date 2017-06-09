# Programmer: Zailyn Tamayo 

# This program will prompt the user to enter two integers.  
# It will then output which is the larger number that was entered.  
# For example, if the user enters 4 and 8, the output will read "8 is the maximum".

first = input("\nEnter the first integer: ")

second = input("\nEnter the second integer: ")

if first > second:
  print ("\n", first, "is the maximum.")
elif first == second:
  print ("\nThey are equal.")
else:
  print ("\n", second, "is the maximum.")
