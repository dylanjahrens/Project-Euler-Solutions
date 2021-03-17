def prime_summer(number):
    #will give sum of primes under given variable 'number'
    primes = 0

    for n in range(2, number):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            primes += n
            
    print('Total sum: ', primes)

prime_summer(10)