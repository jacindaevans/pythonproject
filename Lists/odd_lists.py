jacindaslist = [1,2,3,4,5,6,7,8,9,10]
oddlist =[]
for num in jacindaslist:
    if (num % 2) !=0:
        oddlist.append(num)
        print(num, end=' ')
print (oddlist)