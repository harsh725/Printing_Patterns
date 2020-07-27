num=int(input("Enter size"))
low=0
high=num-1
n=1
count=int((num+1)/2)
nlist=[[0 for i in range(num)]for j in range(num)]
for i in range(count):
    for j in range(low,high+1):
        nlist[low][j]=n
        n=n+1
    for j in range(low+1,high+1):
        nlist[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        nlist[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        nlist[j][low]=n
        n=n+1
    low+=1
    high-=1

for i in range(num):
    for j in range(num):
        print(nlist[i][j],end='\t')
    print()
