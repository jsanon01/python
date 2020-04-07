"""
https://www.youtube.com/watch?v=wfcWRAxRVBA
"""

class Robot:
    def introduce_self(self):
        print("My name is {}".format(self.name))

kiki = Robot()
kiki.namee = 'tom'.upper()
kiki.color = 'red'
kiki.weight = 40
kiki.introduce_self()
print()
roro = Robot()
roro.name = 'jerry'.upper()
roro.color = 'blue'
roro.weight = 70
roro.introduce_self()
print()
