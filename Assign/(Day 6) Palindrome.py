num=int(input("Enter a number :"))
temp=num
rev=0

while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10

if rev==temp:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
