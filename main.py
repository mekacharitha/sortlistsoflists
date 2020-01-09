lis =[]
n=int(input("Enter the size of list "))
for i in range(0,n):
  lis1=list(map(int,input().split()))
  lis.append(lis1)
lis.sort(key=len)
print(lis)