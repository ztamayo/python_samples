# Programmer: Zailyn Tamayo

# A message box with a button that reads "Resize me".  
# When the button is clicked, the box grows by 1.5.

import tkinter 
from tkinter import * 

def resize(): 
  x = root.winfo_width() * 1.5 
  y = root.winfo_height() * 1.5 
  root.geometry("%dx%d+0+0" % (x, y))
 
root = tkinter.Tk() 

w = tkinter.Button(root, text=' Resize Me ', command=resize) 
w.pack() 
 
root.mainloop() 
 
