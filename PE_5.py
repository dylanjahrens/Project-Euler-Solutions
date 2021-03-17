#Simple program with smaller numbers
x = 10
counter = 0 
newlist = []

while counter < 11:
    if counter == 10 and newlist[-1] == 10:
        print(newlist)
        print('all divisible by ', x-1)
        break
    for num in range(1,11):
        if x % num == 0:
            counter +=1
            if len(newlist) == 10:
                newlist.pop(0)
            newlist.append(num)
        else:
            counter = 0
    x += 1



#Too long to process
x = 20
counter = 0 
newlist = []

while counter < 11:
    if counter == 10 and newlist[-1] == 20:
        break
    for num in range(11,21):
        if x % num == 0:
            counter +=1
            if len(newlist) == 10:
                newlist.pop(0)
            newlist.append(num)
        else:
            counter = 0
    x += 20 

print(x-20)