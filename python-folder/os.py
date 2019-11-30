# This script prints 2 functions

ms = 'microsoft'

bg = 'bill gates'

lx = 'linux'

ux = 'unix'

lt = 'linus torvalds'

def microsoft(): # defining the function
      print(f'{ms.title()} is a proprietary software...')
      print(f'{bg.title()} is the CEO & founder of {ms.title()}  ...')



def linux(): # defining the function
      print(f'{lx.title()} is an open source software and is based on {ux.title()} ...')
      print(f'{lt.title()} is the CEO & founder of {lx.title()}...')

microsoft()# printing (calling) the function

print()

linux() # printing (calling) the function
