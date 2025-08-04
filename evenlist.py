list=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter elements:"))
    list.append(value)
ev_list=[]
for i in list:
    if i%2==0:
        ev_list.append(i)
print("Original list:",list)
print("Even numbers in list:",ev_list) 