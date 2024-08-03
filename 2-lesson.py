#Botirov Davron
import os
os.system('cls')
os.system('color 2')

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i != 0:
            continue
        else:
            return False
    return True
def reverse_number(n):
    return int(str(n)[::-1])
def find_reversed_prime_pairs(limit):
    result = []
    primes = [i for i in range(2, limit) if is_prime(i)]
    for prime in primes:
        teskari = reverse_number(prime)
        if teskari != prime and teskari < limit and is_prime(teskari):
            result.append((prime, teskari))
    return result
limit = 100
son = find_reversed_prime_pairs(limit)
print("sonlarni teskarilab chiqarish:\n", son)


