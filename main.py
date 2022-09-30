__copyright__ = "Copyright (C) Hannu Soini"
__author__ = "Hannu Soini"
__version__ = 0, 0, 1
__date__="2022-09-30"
__description__="First beta version"

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# racingstats
# todo numpy / pandas routines
# todo new variable for treeview only for filtering
# todo develop selection routine

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog

DEBUGGER_MODE=True
df=pd.read_csv('road.csv')


def quit(root):
    #if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        exit()
        root.destroy()
    #return

def load_file():
    #try:
        #Loads into racedata list
        with open('road.csv', 'r') as f:
            racedata = [] #init list
            for line in f.readlines():
                racedata.append(line.rstrip().split(","))
            datasize=len(racedata)
            print("File is loaded. Size is", datasize, "races.")
            print(racedata[1:10])
            print(racedata[0])
            #first = Label(frame, text="File is loaded.")
            #first.pack()
        if DEBUGGER_MODE==True:
            with open('checksum.txt', 'w') as f:  # with closes files automatically afterwards. a append w overwrite r read
                f.write(str(racedata)) #Write all lines
#               f.write(str(racedata[1:10]))
#               f.write(f'Data size is {datasize}')
        return racedata
    #except:
    #    print("Could not load file.")

def change_filter(racedata):
    # todo filter by track
    # change this into filter

    pass
    #second = Label(frame, text='Change Track 2', wraplength=1200)
    #second.pack()

def change_value(data):
    #change this into filtered value
    pass
    #print("View car")
    #print(data.split(","))

def add():
    return
    #todo tkinter form

#     race = input("Race id: ")
#     pos = input("Position: ")
#     with open('road.txt', 'a') as f:  # with closes files automatically afterwards. a append w overwrite r read
#         f.write(race + "|" + pos + "\n")

#
# Main program here
#

#tkinter main_window initialisation
main_window = Tk()

# get the screen dimension
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

#Set window size
window_width = int(screen_width*0.5)
window_height = int(screen_height*0.9)

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

main_window.title("iRacingStats - By Kristian Soini 2022")

#textPad = ScrolledText(main_window, width=10, height=10)
#textPad.pack()

frame = Frame(main_window)
frame.pack()
frame.grid(row=0, column=0)
text = Text(frame, width=window_width, height=window_height)
#text.pack()
text.grid(row=4, column=0)

## Frames
#top_frame = Frame(main_window, width=300, height=50, pady=3)
#bottom_frame = Frame(main_window, width=300, height=50, pady=3)

#main_window.grid_rowconfigure(1, weight=1)
#main_window.grid_columnconfigure(0, weight=1)

#top_frame.grid(row=0, sticky="ew")
#bottom_frame.grid(row=4, sticky="e")

RACEDATA = load_file()
nr_columns=len(RACEDATA[0])
nr_lines=len(RACEDATA)
active_filter=''
filter_value=''
print(type(RACEDATA))
#

if DEBUGGER_MODE == True:
    with open('tree.txt', 'w') as f:  # with closes files automatically afterwards. a append w overwrite r read
        f.write(str(f'{RACEDATA[0]} \n'))
        f.write(str(f'Nr of columns is {nr_columns} \n'))
        for n in range(len(RACEDATA[0])):
            f.write(str(f'Column {n} is {RACEDATA[0][n]} \n'))

#Define treeview
#
# Make list of column indexes
columns = []
for n in range(nr_columns):
    columns.append(f'col_{n}')

tree = ttk.Treeview(main_window, columns=columns, show='headings')
# define headings
for n in range(nr_columns):
    tree.heading(f'col_{n}', text=RACEDATA[0][n])

# add data to the treeview
for line in range(1,nr_lines):
    tree.insert('', tk.END, values=RACEDATA[line])

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        #record = item[] #'col_2']
        # show a message
        showinfo(title='Information', message='Selection is'.join(item))
        #showinfo(title='Information', message=','.join(record))

tree.bind('<<TreeviewSelect>>', item_selected)

#tree.pack()

# add a scrollbar
#scrollbar = ttk.Scrollbar(main_window, orient=tk.VERTICAL, command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
#scrollbar.pack() #grid(row=0, column=1, sticky='ns')


# Window layout
button_filter = Button(text, text="Change Filter", command=lambda: change_filter(RACEDATA))
#button.pack()
button_value = Button(text, text="Change Value", command=lambda: change_value(RACEDATA))
#button.pack()
label_first = Label(frame, text=f'Dataset has {len(RACEDATA)} line items.')
#first.pack()
label_second = Label(frame, text=f'Active filter is {active_filter} and the filter value is {filter_value}.')
#second.pack()
button_value.grid(row=0, column=0)
button_value.grid(row=0, column=1)
label_first.grid(row=1, column=1)
label_second.grid(row=2, column=1)
tree.grid(row=3, column=0)


# Menubars
menubar = Menu(main_window)
filemenu = Menu(menubar)
filemenu.add_command(label='Load', command=lambda: load_file())
filemenu.add_command(label='Quit', command=lambda: quit(main_window))
menubar.add_cascade(label='File', menu=filemenu)
main_window.config(menu=menubar)

main_window.mainloop()