# racingstats
# todo file i/o

def view():
    try:
        with open('road.txt', 'r') as f:
            for line in f.readlines():
                data= line.rstrip()
                race, pos = data.split("|")
                print(race, " | ", pos)
    except:
        print("Could not open file.")

def add():
     race = input("Race id: ")
     pos = input("Position: ")
     with open('road.txt', 'a') as f:  # with closes files automatically afterwards. a append w overwrite r read
         f.write(race + "|" + pos + "\n")

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
