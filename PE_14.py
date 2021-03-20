#what number less than one-million produces the longest Collatz sequence
#will list the largest sequence as it counts to one-million

max_chain = 10

for n in range(13,1000001):
    
    number = n
    chain = 1 
     
    while number != 1:    
        if number %2 == 0:
            number = number/2
            chain+=1
        else: 
            number = number * 3 + 1
            chain+=1
    if chain >= max_chain:
        max_chain = chain
        print('Biggest chain so far is',n, 'at', chain)