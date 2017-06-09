# Programmer: Zailyn Tamayo

# Generates a list of five random numbers ranging from 1-30.
 
import random

# Define function
def getNumber():
   i = str(random.randint(0,30))
   return i

print("Content-Type: text/html\n")

print("<html><body>");

print("Super Lotto Numbers: \n");

for x in range(5):
   print(getNumber());

print("</body></html>"); 
