

hollywood = {
		'queen latifah' : 'new jersey',
		'jazzy' : 'new york',
		'top adlerman' : 'haiti',
		'lojy baby' : 'petion ville',
		'ada' : 'nigeria'
		}

for key in sorted(hollywood.keys()):
    print(f'They are all artists: {key.title()}')

print() 

for value in sorted( hollywood.values()):
    print(f'They are from {value.title()} respectively')
