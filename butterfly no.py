n=17
row=0
col=0
last=n
k=1
c=0
j=0
l=[[' ' for i in range(20)]for j in range(20)]
for i in range(0,n):
    j=i
    col=i
   # print(last,j)
    while(j<last):
       l[j][col]=i+1
       j+=1
    last-=1
    col+=1
n=n//2

for i in range(n,-1,-1):
    j=i
    col=i
   # print(last,j)
    while(j<last):
       l[j][col]=i
       j+=1
    last+=1
    col+=1


for i in range(17):
    for j in range(17):
        print(l[i][j],end='')
    print()
    
        
