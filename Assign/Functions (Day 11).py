# amstrong number:

def ams(num):
  r=0
  temp=num
  
  while num>0:
    n=num%10
    r+=n**3
    num=num//10

  if temp==r:
    print("its an amstrong number")
  else:
    print("Its not an amstrong number")

num=int(input("Enter a number :"))
ams(num)


#sum of given numbers:

def add(*numbers):
    tot = 0
    for num in numbers:
        tot += num
    return tot

n = int(input("Enter the total count :"))
numbers = []

for i in range(n):
    num = int(input("Enter number"+ str(i+1)+ ": "))
    numbers.append(num)

print("Total Sum :",add(*numbers))


#palindrome:

def palindrome(num):
    temp=num
    rev=0

    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10

    if rev==temp:
        return True
    else:
        return False


num=int(input("Enter a number :"))
result=palindrome(num)

if result:
    print("It's a palindrome")
else:
    print("It's not a palindrome")



#fibonacci:

def fib(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

num = int(input("Enter the number :"))
fib(num)




