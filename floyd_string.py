#Triangle pattern
n=(input("Enter string"))
l=len(n)
for i in range(l+1):
    for j in range (l):
        if j<i:
            print(n[j],end='')
    print()
