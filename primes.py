'''Solving a Worldwide Center of Mathematics problem
Distinct prime numbers p,q,r satisfy the equation
2pqr + 50pq = 7pqr + 55pr = 8pqr + 12qr = A
for some positive integer A. What is A?
'''

from math import sqrt
from random import sample
from itertools import permutations

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,int(sqrt(num)+1),2):
        if num % i == 0:
            return False
    return True

primeList = [i for i in range(2,5000) if isPrime(i)]

#count = 0

#while count < 1000000:

perms = permutations(primeList,3)

for p,q,r in perms:

    if 2*p*q*r + 50*p*q == 7*p*q*r and 7*p*q*r + 55*p*r == 8*p*q*r + 12*q*r:
        print(p,q,r,2*p*q*r + 50*p*q)
        break
    
