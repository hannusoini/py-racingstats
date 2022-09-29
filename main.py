# racingstats
# todo file parsing
# todo numpy routines
# todo gui

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog

def quit(root):
    #if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        exit()
        root.destroy()
    #return

def load_file():
    #try:
        races=[]
        #todo fix load routine. Loads only last line
        with open('road.csv', 'r') as f:
            for line in f.readlines():
                #first
                racedata=[]
                for n in line:
                    racedata.append(line.rstrip().split(","))
                races.append(racedata)
                #race, pos = data.split(",")
                #print(race, " | ", pos)
            datasize=len(races)
            print("File is loaded. Size is", datasize, "races.")
            print(races[:][0])
            print(races[0][0])
            #first = Label(frame, text="File is loaded.")
            #first.pack()
        return races
    #except:
    #    print("Could not load file.")

#contacts = []
#for n in range(1, 100):
#    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com', f'date {n}'))

def change_track(data):
    # todo display data in tkinter multi-column list
    first = Label(frame, text="Change Track")
    first.pack()
    second = Label(frame, text='Change Track', wraplength=1200)
    second.pack()

#    mode = input("View Car, View Track: (C/T)").lower()
#    if mode == "c":
#        print("Car ")
#    elif mode == "t":
#        print("Track ")
def change_car(data):
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

window_width = 800
window_height = 600

# get the screen dimension
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

main_window.title("iRacingStats - By Kristian Soini 2022")

#textPad = ScrolledText(main_window, width=10, height=10)
#textPad.pack()

frame = Frame(main_window)
frame.pack()
text = Text(frame, width=window_width, height=window_height)
text.pack()

## Frames
#top_frame = Frame(main_window, width=300, height=50, pady=3)
#bottom_frame = Frame(main_window, width=300, height=50, pady=3)

#main_window.grid_rowconfigure(1, weight=1)
#main_window.grid_columnconfigure(0, weight=1)

#top_frame.grid(row=0, sticky="ew")
#bottom_frame.grid(row=4, sticky="e")

data = load_file()
print(type(data))
#
#Define treeview
#
columns = ('race_id', 'season', 'week', 'date')
tree = ttk.Treeview(main_window, columns=columns, show='headings')
# define headings
tree.heading('race_id', text='Race ID')
tree.heading('season', text='Season')
tree.heading('week', text='Week')
tree.heading('date', text='Date')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com', f'date {n}'))

# add data to the treeview #todo add data from file here
for contact in contacts:
    tree.insert('', tk.END, values=contact)
#each character is a line
#for race in races:
#    tree.insert('', tk.END, values=race)
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

tree.bind('<<TreeviewSelect>>', item_selected)
tree.pack()

# add a scrollbar
#scrollbar = ttk.Scrollbar(main_window, orient=tk.VERTICAL, command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
#scrollbar.pack() #grid(row=0, column=1, sticky='ns')


# Window layout
button = Button(text, text="Change Track", command=lambda: change_track(data))
button.pack()
button = Button(text, text="Change Car", command=lambda: change_car(data))
button.pack()
first = Label(frame, text="All date")
first.pack()

# Menubars
menubar = Menu(main_window)
filemenu = Menu(menubar)
filemenu.add_command(label='Load', command=lambda: load_file())
filemenu.add_command(label='Quit', command=lambda: quit(main_window))
menubar.add_cascade(label='File', menu=filemenu)
main_window.config(menu=menubar)

main_window.mainloop()