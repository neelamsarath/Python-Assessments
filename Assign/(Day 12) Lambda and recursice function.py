#Lambda function ( Odd or Even ):

oddoreve = lambda n:n%2 

num = int(input("Enter a number :"))
result=oddoreve(num)

if(result==0):
          print("Its even number")
else:
    print("Its a odd number")


#Lambda Function ( odd or Even with ternary operator ):

oddoreven=lambda x:"Even" if x%2==0 else "Odd"
nums=int(input("Enter a number :"))
print(oddoreven(nums))


#Sum of digit using recursion function:

def sum(n):
    if n==0:
        return 0
    else:
        result = (n%10) + sum(n//10)
        return result

num = int(input("Enter a number :"))
print(sum(num))

'''
def name(*a):
    for i in a:
        print(i)

name(10,20,30)

#defaul parameter:
def display(a=10,b=20):
    print(a,b)

display(100,200)

#lambda:
result=lambda a:a*100
print(result(10))


#recursion:
def factorial(number):
    if number==1:
        return 1
    else:
        result = number * factorial(number - 1)
    return result
print(factorial(5))

'''





