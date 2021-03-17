# Largest palindrome of 2 triple digit numbers

y = 100
palindromes = []

while y < 999:
    for x in range(100,1000):
        z= x*y
        if str(z) == str(z)[::-1] and z not in palindromes:
            palindromes.append(z)
    y+=1

order = sorted(palindromes)
print('Largest Palindrome = ', order[-1])