# Script is about a colection-controlled loop


# 1) a list 
artists = ['Toussaint Louverure', 'Dessaline Ambroise', 'denis', 'ti-ra', 'ti-pay']
print("Printing list with words's length")
# 2) For statement along with length of words
for artist in artists:
    print(f'{artist.title()} = {len(artist)} words')
