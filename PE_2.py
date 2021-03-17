#terms in the Fibonacci sequence under four million, find the sum of the even-valued terms

fib = [1,2]
x = fib[-1] + fib[-2]

while fib[-1] < 4000000:
    next_num = fib[-1] + fib[-2]
    if next_num < 4000000:
        fib.append(next_num)
    else:
        break

even_fibs = []
for n in fib:
    if n %2 == 0:
        even_fibs.append(n)
        
print(even_fibs)

print(sum(even_fibs))
