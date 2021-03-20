def triangle_numbers(x):

#will give the triangle numbers up to x
#goal is to find the first tirangle number with over 500 divisors
#algorithmic approach takes too long to solve
#28 is the 7th number (1+2+3+4+5+6+7)
    
    tri_num = 0
    
    for n in range(1, x+1):
        divisors = 0
        tri_num += n
        for i in range(1, tri_num+1):
            if tri_num % i == 0:
                divisors +=1
        print('Triangle number ', n, 'is ', tri_num, ',  Divisors: ', divisors)
        if divisors > 500:
            print('Triangle number ', tri_num, ' is the first with over 500 divisors!')