'''
import threading
import time

def res_order():
    print("Order your food")
    time.sleep(4)
    print("Food is served")

def res_preparation():
    print("Preparation time takes longer")
    time.sleep(2)
    print("Ordered food is currently unavailable")

t1=threading.Thread(target=res_order)
t2=threading.Thread(target=res_preparation)

t1.start()
t2.start()
'''

import threading
import time

def res_order():
    for i in range(1,10):
        print("No.of Orders: ",i)
        time.sleep(3)
    
def res_preparation():
    for i in range(1,10):
        time.sleep(1)
        print(f"It takes {i} hours")
        

t1=threading.Thread(target=res_order)
t2=threading.Thread(target=res_preparation)

t1.start()
t2.start()
