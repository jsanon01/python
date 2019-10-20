# This script print usernames info

users = {
	'aeistein@gmail.com' : {
	'first' : 'albert',
	'last' : 'eistein',
	'location' : 'paris, france'},

	'apierre@yahoo.fr' : {
        'first' : 'ana-maria',
        'last' : 'jose',
        'location' : 'barcelona, spain'},

        'evilaire@yahoo.ht' : {
        'first' : 'etzer',
        'last' : 'vilaire',
        'location' : 'jeremie, haiti'},
	
	}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = f"{user_info['location'].title()}"
    
    print(f'\tFull name: {full_name}')
    print(f"\tLocation: {location}")
