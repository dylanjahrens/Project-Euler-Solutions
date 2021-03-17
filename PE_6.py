sum_of_squares = 0
sums = 0

#sum_of_squares

for x in range(1,101):
    product = x**2
    sum_of_squares += product
print(sum_of_squares)

#square_of_sums

for y in range(1,101):
    sums += y

square_of_sums = sums**2
print(square_of_sums)
    
#difference = square_of_sums - sum_of_squares

difference = square_of_sums - sum_of_squares

print(difference)