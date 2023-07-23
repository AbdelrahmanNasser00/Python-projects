##Binary search
##goal: search whether a given number is present in the string or not
##topics: list,sorting,search
import numpy as np
lst=[]
n=int(input("Enter size of list\n"))
lst.sort()
first=0
last=n-1
mid=(first+last)/2
found=False
##input list
print("Enter list elements")
for i in range(0,n):
    temp=int(input())
    lst.append(temp)
##take the number from user
item=int(input("Enter number "))
while(first<=last and not found):
    mid=(first+last)//2 ## //=>mean divide and take floor
    if lst[mid]==item:
        print(f"number has been found and it's location is {mid}")
        found=True
    else:
        if item < lst[mid]:
            last=mid-1
        else:
            first=mid+1
if found is False:
    print("Not found")