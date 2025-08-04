n=int(input("enter no of elements: "))
a=[]
b=[]
print("Enter element")
for i in range(n):
    temp=input()
    a.append(temp)
print("List :",a)

flag=0
 
for i in range(n):
    for j in range(n):
        if(i==j):
            continue
        if(a[i]==a[j]):
            flag=1
    if(flag==0):
        b.append(a[i])
    flag=0
print("unique element List :",b)