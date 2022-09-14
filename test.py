import random

num_of_passwords = 0

while num_of_passwords != 3:
	ltp = ''
	for i in range(4):
	  ltp += str(random.randint(0, 9))
	  print(ltp)
	
	print(ltp)
	print()

	num_of_passwords += 1