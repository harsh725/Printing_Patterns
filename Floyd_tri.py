#Floyd's Triangle
x=1
n=int(input('Enter no of rows'))
for i in range(n):
    for j in range(n):
        if j<i:
            print(x,end=' ')
            x+=1
    print()
