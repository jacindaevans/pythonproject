jacindaslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = []
for num in jacindaslist:
    if (num % 2) ==0:
        evenlist.append(num)
        print(num, end=' ')
print(evenlist)
