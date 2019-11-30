# This script prints username + user_info from a dictionary

users = {
	'ksanon@gmail.com' : {
	'first':'kristel',
	'last' : 'salomon',
	'location' : 'norton',
	'zip_code' : '33055'
	}
	}

for user, user_info in users.items():
    print(f'\tUsername:\t{user}')
    full_name = f"\t{user_info['first']} {user_info['last']}"
    location = f"\t{user_info['location']}"
    zip_code = f"\t{user_info['zip_code']}"

    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')
    print(f'\tZip-Code: {zip_code}')
