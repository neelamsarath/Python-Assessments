class Sarath(Exception):
    pass

num=int(input("Enter a number :"))
a=[1,2,3,4,5,6]

try:
    if num in a:
        raise Sarath("The number is present")
    else:
        print("The number not present")
        print(x)

except Sarath as sa:
    print(sa)
