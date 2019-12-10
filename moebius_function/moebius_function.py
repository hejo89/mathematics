from random import choice
from math import sqrt, log
import matplotlib.pyplot as plt


exp = 6
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

primes = foo(10**exp)
prime_set = set(primes)	

factorization = {}
def f(n):
	if n in prime_set:
		factorization[n] = {n: 1}
		return
	for p in primes:
		if n / p in factorization and n % p == 0:
			if p in factorization[n / p]:
				tmp = factorization[n / p].copy()
				tmp[p] += 1
				factorization[n] = tmp
			else:
				tmp = factorization[n / p].copy()
				tmp[p] = 1
				factorization[n] = tmp
			return
			
for k in range(2, 10**exp + 1):
	f(k)

def moebius_function(n):
	if n == 1: return 1
	c = 0
	for k in factorization[n]:
		c += 1
		if factorization[n][k] > 1: return 0
	if c % 2: return -1
	return 1

def mertens_function(n):
	s = 0
	for j in range(1, n + 1):
		s += moebius_function(j)
	return s

numbers = []
s = 0
for _ in range(1, 10**exp + 1):
    s += moebius_function(_)
    if _ % 10**4 == 0: numbers.append(s)
#    numbers.append(s)
x_axis = range(10**4, 10**exp + 1, 10**4)
plt.plot(x_axis, numbers)
plt.ylabel('some numbers')


plt.plot([0.43*sqrt(k) for k in range(10**exp)])
plt.plot([-0.43*sqrt(k) for k in range(10**exp)])


#for _ in range(3):
#	s, rw, coin_flip = 0, [], [-1, 1]
#	for j in range(10**7):
#		s += choice(coin_flip)
#		rw.append(s)

#	plt.plot(rw)
#plt.plot([sqrt(2*k*log(log(k))) for k in range(16, 10**7+16)])
#plt.plot([-sqrt(2*k*log(log(k))) for k in range(16, 10**7+16)])
#plt.plot([1.96*sqrt(k) for k in range(16, 10**7+16)])
#plt.plot([-1.96*sqrt(k) for k in range(16, 10**7+16)])
plt.show()



