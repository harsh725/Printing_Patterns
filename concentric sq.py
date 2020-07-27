#Concentric sq

n=int(input())
r=2*n-1
l=[['*' for x in range(r)]for y in range(r)]

row=0
col=0
last=2*n-2
k=n
for i in range(n):
    for j in range(i,r):
        l[row][j]=k
        l[last][j]=k
        l[j][row]=k
        l[j][last]=k
    row+=1
    last-=1
    k-=1
    r-=1
    
for i in range(2*n-1):
    for j in range(2*n-1):
        print(l[i][j],end='')
    print()
            
        
    
    
