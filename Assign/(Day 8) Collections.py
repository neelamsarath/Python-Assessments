'''
#List

furnitures=["chair","table","Bed","cupboard"]
print("Inputs 1 :",furnitures)

print(type(furnitures))

furnitures.append("Study table")
print("Append :",furnitures)

furnitures.insert(2,"door")
print("Insert :",furnitures)

print("Indexing :",furnitures[2])
print("Slicing :",furnitures[2:5])
print("Reverse :",furnitures[::-1])

furnitures.pop(2)
print("Pop :",furnitures)

furnitures.remove("cupboard")
print("Remove :",furnitures)

print()

electronics=["Mobile","laptop",55]
print("Inputs 2 :",electronics)

electronics.extend(furnitures)
print("Extend() :",electronics)



#Tuples:

furnitures=("chair","table","Bed","cupboard","Bed")
print("Inputs 1 :",furnitures)

print(type(furnitures))
print()
print("Indexing :",furnitures[3])
print("Negative Indexing :",furnitures[-1])
print("Slicing[2,3,4] :",furnitures[2:5])
print("Slicing[0,1,2,3] :",furnitures[:4])
print("Reverse :",furnitures[::-1])

#Adding two tuple:
electronics=("mobile",)
households=furnitures+electronics
print("Adding two tuples :",households)


#loop
for i in range(len(households)):
  print({i},households[i],end="  ")

'''

#Set:

furnitures={"chair","table","Bed","cupboard","Bed"}
print("Inputs 1 :",furnitures)

print(type(furnitures))
print()

furnitures.add("Door")
print("Adding door :",furnitures)

furnitures.add("wooden table")
print("Adding wooden table :",furnitures)

furnitures.remove("cupboard")
print("Remove cupboard:",furnitures)

furnitures.discard("wooden table")
print("Remove wooden table:",furnitures)

furnitures.pop()
print("Pop :",furnitures)

print("Checking whether table is in furnitures :")
print("table" in furnitures)

print()

#Adding two sets:
electronics={"mobile","laptop","55"}
print("Input 2",electronics)

furnitures.update(electronics)
print("Add two sets(Update) :",furnitures)

print("Looping through sets:")
#loop
for i in furnitures:
  print(i,end="  ")
  
print("\n")

car=frozenset({"BMW","Ferrari"})
print("Frozen set :",car)
print(type(car))


  










