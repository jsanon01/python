"""
I want to create a dictionary with key-value pairs
I want to print out these key-value pairs

I want to open an image after running dictionary

"""
from PIL import Image

original = Image.open('vpc_pic.png')

vpc = {
	'vpc	': 'the premises in the cloud',
	'igw	': 'the main or entrance door',
	'route table': 'the main hall',
	'subnets': 'the rooms',
	'nacl	': 'are the door rooms',
	'pub sub': 'the living room',
	'priv sub': 'the bedroom',
	'sec. group': 'the appliance doors',
	'ec2	': 'the appliances',
	'cidr	': 'the street address',
	}
print('\nThis script not only prints out key-value pairs of a dictionary\nbut also automatically opens an image...')

print()

for x, y in vpc.items():
    print("- {}\t metaphorically speaking is {}".format(x,y).title())


original.show()

print()
