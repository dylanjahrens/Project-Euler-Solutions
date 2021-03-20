#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open('euler13input.txt', 'r')
big_number = f.read()

list_of_fifty = big_number.strip().split()

total = 0

for number in list_of_fifty:
    total += int(number)
    
print(total)
print(str(total)[:10])