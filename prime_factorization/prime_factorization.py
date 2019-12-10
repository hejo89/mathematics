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

cache = {}
for j in range(1,10**6 + 1):
	f(j)
print cache
