class Dog:
    def __init__(self):
        self.barks=0
    def bark(self):
        print('bark')
        self.barks=self.barks+1
    def miauo(self):
        print(self.barks)

d = Dog()
d.bark()
for i in range(9):
    d.bark()
d.miauo()