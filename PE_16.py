#What is the sum of the digits of the number 21000?

num = 2**1000
string_of_num = str(num)

total = 0

for digit in string_of_num:
    digit = int(digit)
    total += digit
    
print(total)