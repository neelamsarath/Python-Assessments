s="aaaabbccccdddddfffffff"

count={}

for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for key,value in count.items():
    print(key, ":", value)
