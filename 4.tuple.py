list_a=[]
sorted=[]
n=int(input("Enter no of elements :"))
for i in range(n):
    list_a.append((int(input("num 1 :")),int(input("num 2:"))))
while list_a:
    small=list_a[0]
    for tup in list_a:
        if tup[1]<small[1]:
            small=tup
    sorted.append(small)
    list_a.remove(small)
print("Sorted : ",sorted)