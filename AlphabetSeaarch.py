n=int(input("Enter no of elements.\n"))
arr=[]
print("Enter numbers")
for i in range(n):
    arr.append(ord(input()))
x=ord(input("Enter no you want to search"))
sol=-1
choose=ord(input("Enter 1 for linner search else we will find it by binarry\n"))
if choose==1:
    for i in range(len(arr)):
        if arr[i]==x:
            sol=i+1
            break
else:
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
        print(f"{chr(i)}",end=' ')
    print("\n")
    print(f"Element is present at {sol} position")
