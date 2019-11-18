# This script prints words in a senetnce


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts: 
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print('This script prints words in a sentence')
print(word_count('the house in the little prairie is green...'))

