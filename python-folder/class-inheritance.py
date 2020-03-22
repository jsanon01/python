"""
I want to define a parent class named Fish
I want to define __init__ method with first_name and last_name
I want to define another method named swim()
I want to define a child class named swim_backwards()


"""

class Fish:
    def __init__(self, first_name, last_name='fish'):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print('the fish swims smoothly...')

    def swim_backwards(self):
        print('all fish can swim backwards...')



class Trout(Fish):
    pass

terry = Trout('terry'.upper())

print(terry.first_name)
