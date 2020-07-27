#Number in right triangle shape
n=int(input("Enter no of rows"))
n_list=[[' ' for i in range(n)]for j in range (n)]
x=1
for i in range(n):
    for j in range(i,n):
        n_list[j][i]=x
        x+=1
    

for i in range(n):
    for j in range(n):
        print(n_list[i][j],end='  ')
    print()
