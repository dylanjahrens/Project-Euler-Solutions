#Find the sum of the digits in the number 100!

def factoral(n):
    product = n
    total_sum = 0
    for i in range(1,n):
        product *= i
        
    print('Factoral: ', product)
    
    product_string= str(product)
    
    for i in product_string:
        digit = int(i)
        total_sum += digit
        
    print('Sum of factoral: ', total_sum)

factoral(100)
