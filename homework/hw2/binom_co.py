import time

def main():
	test_vals = [ 4, 8, 10, 16, 20, 25 ]
	bc_one_vals = []
	bc_two_vals = []
	for test_val in test_vals:
		n = test_val
		k = n / 2
		# test bc_one
		start_time = time.time()
		bc_one(n, k)
		bc_one_vals.append((n, time.time() - start_time))
		# test bc_two
		start_time = time.time()
		bc_two(n, k)
		bc_two_vals.append((n, time.time() - start_time))
	for val in bc_one_vals:
		print("[BC1] %u: %s s" % val)
	for val in bc_two_vals:
		print("[BC2] %u: %s s" % val)

def bc_one(n, k):
	if (n == k or k == 0):
		return 1
	return bc_one(n - 1, k) + bc_one(n - 1, k - 1)

def bc_two(n, k):
	if (k == 0):
		return 1
	return bc_two(n - 1, k - 1) * (n / k)

if __name__ == '__main__':
	main()