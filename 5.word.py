sen=input("enter String: ")
words=sen.split()
count=0
for word in words:
    for j in words:
        if word == j:
            count+=1
print(count)