# racingstats
# todo file i/o

def view():
    pass

def add():
    pass

while True:
    mode = input("Add new or View data or Quit (A/V/Q)? ").lower()
    if mode =="q":
        break
    elif mode =="v":
        view()
    elif mode =="a":
        add()
    else:
        print("Invalid selection.")
        continue
