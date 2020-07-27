#   1
#   2   9   
#   3   8   10
#   4   7   11  14  
#   5   6   12  13  15

n=int(input("Enter no of rows"))
n_list=[[' ' for i in range(n)]for j in range(n)]
x=1
s=(n*(n+1))/2
c=int((n+1)/2)
col=0
start=0

for i in range(0,n,2):
    for j in range(start,n):
        n_list[j][col]=x
        x+=1
    col+=1
    if x==s+1:break
    for j in range(n-1,i,-1):
       # print(x)
        n_list[j][col]=x
        x+=1
   # print()
    col+=1
    start+=2
    if x==s+1:break

for i in range(n):
    for j in range(n):
        print(n_list[i][j],end='  ')
    print()
