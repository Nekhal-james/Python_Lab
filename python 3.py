n=int(input("enter no of elements: "))
a=[]
print("Enter element")
for i in range(n):
    a.append(int(input()))
print("List :",a)
b=[]
for i in range(n):
    if(a[i]%2==0):
        b.append(a[i])
print("even List :",b)