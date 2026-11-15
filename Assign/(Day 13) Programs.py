#Amstrong numbers from 1 to 1000:

for i in range(1, 1001):
    temp = i
    l = 0
    s = 0

    while temp > 0:
        l += 1
        temp //= 10
    temp = i

    while temp > 0:
        rem = temp % 10
        s += rem ** l
        temp //= 10

    if s == i:
        print(i, end=" ")

'''
#palindrome numbers from 1 to 1000:
        
for i in range(1, 1001):
    temp = i
    rev = 0

    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp //= 10

    if rev == i:
        print(i, end=" ")

'''

