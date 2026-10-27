row=4
column=7
space=row-1


for i in range(1,row+1):  #i=(1,4) 1 2
    for z in range(1,space+1):
        print(" ",end=" ")
    for j in range(1,column+1): #j=(1,2) (1,4) (1,6)
        print("*",end=" ")
 
    column=column-2
    space=space+1
    print("\n",end="")
