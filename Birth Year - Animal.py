# Programmer: Zailyn Tamayo; Date: 05/02/2013

# A message box will prompt the user to input 
# the year they were born.  It will output what 
# animal sign they are according to the Chinese Zodiac.
 
y = int (input("\nEnter the year you were born (e.g. 1980): ")) 
 
print("\nYou were born in"),  
 
if (y%12 == 0): print("monkey"), 
elif (y%12 == 1): print("rooster"), 
elif (y%12 == 2): print("dog"), 
elif (y%12 == 3): print("pig"), 
elif (y%12 == 4): print("rat"), 
elif (y%12 == 5): print("ox"), 
elif (y%12 == 6): print("tiger"), 
elif (y%12 == 7): print("hare"),
elif (y%12 == 8): print("dragon"), 
elif (y%12 == 9): print("snake"), 
elif (y%12 == 10): print("horse"), 
else: print("goat"), 
 
print("year!"); 
