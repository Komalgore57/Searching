n=int(input("Enter no of elements.\n"))
arr=[]
print("Enter numbers")
for i in range(n):
    arr.append(int(input()))
x=int(input("Enter no you want to search"))
sol=-1
arr.sort()
i=0
j=len(arr)-1
while(i<=j):
    mid=(i+j)//2
    if arr[mid]==x:
        sol=mid+1
        break
    elif arr[mid]>x:
        j=mid-1
    else:
        i=mid+1
if sol==-1:
    print("Not Found")
else:
    for i in arr:
        print(f"{i}",end=' ')
    print("\n")
    print(f"Element is present at {sol} position")

