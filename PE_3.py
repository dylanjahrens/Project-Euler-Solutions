#Outputs all prime numbers under variable number
def prime_counter(number):
    primes = []
    for n in range(2, number):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            primes.append(n)
    
    print(primes)




#Only output is highest number
def largest_prime(number):
    for n in reversed(range(2, number)):
        for i in reversed(range(2, n)):
            if (n % i) == 0:
                break
        else:
            print(n)
            return


prime_counter(29)
largest_prime(29)   