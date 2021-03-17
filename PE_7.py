def prime_counter(number):
    #algorithmic approach is too slow to process the 10001st prime number
    primes = []

    for n in range(2, number):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            primes.append(n)

    print(primes[10000]) 
    #will print the 10001 prime number