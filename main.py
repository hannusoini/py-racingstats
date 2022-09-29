# racingstats
# todo file parsing
# todo gui

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog

def cross(text):
    text.insert(INSERT, 'Race 1: ')

def quit(root):
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        exit()
        root.destroy()
    return

def load_file():
    try:
        with open('road.csv', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                #print(data.split(","))
                #race, pos = data.split(",")
                #print(race, " | ", pos)
        print("File loaded.")
        return data
    except:
        print("Could not open file.")


def view(data):
    print("View data")
#    mode = input("View Car, View Track: (C/T)").lower()
#    if mode == "c":
#        print("Car ")
#    elif mode == "t":
#        print("Track ")
#    return
def view_car():
    print(data.split(","))
    pass



def add():
    return
#     race = input("Race id: ")
#     pos = input("Position: ")
#     with open('road.txt', 'a') as f:  # with closes files automatically afterwards. a append w overwrite r read
#         f.write(race + "|" + pos + "\n")

# while True:
#    mode = input("View, Add data or Quit (V/A/Q)? ").lower()
#    if mode =="q":
#        break
#    elif mode =="v":
#        view(data)
#    elif mode =="a":
#        add()
#    else:
#        print("Invalid selection.")
#        continue

#
# Main program here
#
data = load_file()

#tkinter initialisation
main_window = Tk()
main_window.minsize(300,100)
main_window.geometry('{}x{}'.format(800, 600))
main_window.title("iRacingStats - By Kristian Soini 2022")

#textPad = ScrolledText(main_window, width=100, height=80)
#textPad.pack()

frame = Frame(main_window)
frame.pack()
text = Text(frame, height=1000, width=1000) # init text frame in window
text.pack()

# Menubars
menubar = Menu(main_window)
filemenu = Menu(menubar)
filemenu.add_command(label='Load', command=lambda: load_file())
filemenu.add_command(label='Quit', command=lambda: quit(main_window))

menubar.add_cascade(label='File', menu=filemenu)
main_window.config(menu=menubar)

button = Button(text, text="View Track", command=lambda: view_car(data))
button.pack()
button = Button(text, text="View Car", command=lambda: view(data))
button.pack()

main_window.mainloop()