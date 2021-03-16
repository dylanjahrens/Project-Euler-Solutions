#Sum of multiples of 3 or 5 below 1000

numbers = []
for num in range(1,1000):
    if num % 3 == 0 or num % 5 == 0:
        numbers.append(num)

print(sum(numbers))


