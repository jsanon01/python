# This script is about a function that 
# Not only includes for-loop but also sort aplhabeticlly

tvs = ['cnn','fox','pvs','pluriel','eclair','macaya','abc']

tvs.sort()

def my_tv(tvs):
    for tv in tvs:
        print(tv.upper())
        

my_tv(tvs)
