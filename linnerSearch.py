n=int(input("Enter no of elements.\n"))
arr=[]
print("Enter numbers")
for i in range(n):
    arr.append(int(input()))
x=int(input("Enter no you want to search"))
sol=-1

for i in range(len(arr)):
    if arr[i]==x:
        sol=i+1
        break
if sol==-1:
    print("Not Found")
else:
    for i in arr:
        print(f"{i}",end=' ')
    print("\n")
    print(f"Element is present at {sol} position")
