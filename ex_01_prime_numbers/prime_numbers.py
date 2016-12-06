def prime_numbers():
    primes = [2]
    for x in range(3, 500):
        if any(x % y == 0 for y in range(2, x)):
            continue
        primes.append(x)
    return primes
