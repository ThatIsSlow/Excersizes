""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

# Using pathlib and OS to create directories and add files
from pathlib import Path
import os
# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
   message= "Your folder name is "+ entry.get()
   message1= "Your file name is "+ entry1.get()
   message2= "Your file content is "+ entry2.get()
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   label1= Label(frame, text= message1, font= ('Times New Roman', 14, 'italic'))
   label2= Label(frame, text= message2, font= ('Times New Roman', 14, 'italic'))
   label.pack(side = TOP)
   label1.pack(side = TOP)
   label2.pack(side = TOP)
   print(Path.cwd())

   chosen_dir = str(entry3.get()) 
   os.chdir(chosen_dir)
   print(Path.cwd())
   chosen_dir = chosen_dir + '\ '
   Folder_name = chosen_dir + str(entry.get())
   os.makedirs(Folder_name)
   os.chdir(Folder_name)
   print(Path.cwd())
   File_name = str(entry1.get()) + ".txt"
   p = Path(File_name)
   text_in_file = str(entry2.get())
   p.write_text(text_in_file)
   p.read_text()
   

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an entry to direct folder to a certain directory
entry3 = ttk.Entry(frame, width= 40)
entry3.insert(INSERT, "Please paste your chosen Direrctory")
entry3.pack()

#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Name your folder")
entry.pack()

#Create another entry widget
entry1 = ttk.Entry(frame, width= 40)
entry1.insert(INSERT, "Name your file")
entry1.pack()

#Create another entry widget
entry2 = ttk.Entry(frame, width= 40)
entry2.insert(INSERT, "Place content in your file")
entry2.pack()



#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()