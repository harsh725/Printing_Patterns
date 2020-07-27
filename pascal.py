num=int(input("Enter no of rows:"))
for i in range(1,num+1):
    print(end=' '*(num-i))
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()

for i in range(num-1,0,-1):
    print(end=' '*(num-i))
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()
 
