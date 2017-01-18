def hash_maker(service = None, hash_min=4, hash_max=6):
	import random, string

	hash_long = random.randint(hash_min, hash_max)
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(hash_long))