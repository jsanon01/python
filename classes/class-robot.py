"""
I want to create a class named Robot
I want to create a method named introduce_self
I want to instantiate kiki as object inside the class named Robot
I want to create the following class attributes:
- name, color, weight
I wamt to call or print out the method

https://www.youtube.com/watch?v=wfcWRAxRVBA
"""

class Robot:
    def introduce_self(self):
        print("\nMy name is {}".format(self.name))

r1 = Robot()
r1.name = 'junia pierre'.title()
r1.color = 'white'
r1.weight = 79
r1.introduce_self()


kiki = Robot()
kiki.name = 'tom & jerry'.upper()
kiki.color = 'red'
kiki.weight = 40
kiki.introduce_self()

roro = Robot()
roro.name = 'vlad bazile'.upper()
roro.color = 'blue'
roro.weight = 70
roro.introduce_self()
print()
