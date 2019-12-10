from math import sqrt

def foo(n):
	j, primes = 5, [2, 3]
	for j in range(5, n + 1):
		for p in primes:
			if p > sqrt(j):
				primes.append(j)
				break
			if j % p == 0: break
		j += 1
	return primes

primes = foo(10**6)
primes_set = set(primes)	

def f(n):
	if n == 1: return [1]
	if n in primes_set:
		cache[n] = [1, n]
		return cache[n]

	for p in primes:
		if n / p in cache and n % p == 0:
			cache[n] = cache[n / p] + [p]
			return cache[n]


divisor = {}

cache = {1:[1]}
a = []
for j in range(2,10**6 + 1 + 1):
	f(j)

for j in cache:
	c = 1
	for k in set(cache[j][1:]):
		c *= cache[j].count(k) + 1
	a.append((c, j))

print cache
