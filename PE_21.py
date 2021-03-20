#Evaluate the sum of all the amicable numbers under 10000.

def amicable(x):
    
    #gives the sums of amicable numbers up to number x
    
    amicable_total = 0
    
    for number in range(1, x):
        divisors = []
        for i in range(1, number):
            if number % i == 0:
                divisors.append(i)
        divisor_sum = sum(divisors)
        
        #to find if second number matches
        #divisor_sum will be == number2 and then we need: number == divosor_sum2
        
        if divisor_sum < x :    
            divisors2 = []
            for i2 in range(1, divisor_sum):
                #WHY DOES UPPER LIMIT NEED TO BE DIVISOR_SUM???
                if divisor_sum % i2 == 0:
                    divisors2.append(i2)
            divisor_sum2 = sum(divisors2)
                
        if divisor_sum2 == number and number < divisor_sum:
            amicable_total += (number + divisor_sum)
            print('Amicable numbers:',number, divisor_sum)
    print('Amicable total:', amicable_total) 

amicable(10000)