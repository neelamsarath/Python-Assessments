#Multilevel Inheritance
'''
#Sample 1:
class Bhaahubali:
    def grandmother(rajamouli):
        print("Sivagami Devi was the grandmother of Mahindra Bhaahubali")
        
class Bhaahubali1(Bhaahubali):
    def parent(rajamouli):
        print("Amarendra Bhaahubali and Devasena was the parent of Mahendra Bhaahubali")

class Bhaahubali2(Bhaahubali1):
    def child(rajamouli):
        print("Mahendra continued ruled the Mahishmathi after the war")

b1=Bhaahubali2()
b1.grandmother()
b1.parent()
b1.child()

'''


#Sample 2
class Bhaahubali:
    def __init__(rajamouli):
        rajamouli.queen="Sivagami"

    def display(rajamouli):
        print(f"{rajamouli.queen} ruled the mahistmati")


class Bhaahubali1(Bhaahubali):
    def __init__(rajamouli):
        super().__init__()
        rajamouli.king1="Amarendra"
        rajamouli.queen1="Devasena"

    def display(rajamouli):
        super().display()
        print(f"{rajamouli.king1} was meant to rule the mahistmati but unfortunately he didn't")

class Bhaahubali2(Bhaahubali1):
    def __init__(rajamouli):
        super().__init__()
        rajamouli.king2="Mahendra"
        rajamouli.queen2="Avantika"

    def display(rajamouli):
        super().display()
        print(f"{rajamouli.king2} was the son of {rajamouli.king1} and he ruled the mahistmati")

b1=Bhaahubali2()
b1.display()



#Multiple Inheritance:

class parthiban:
    def lead1(loki):
        print("Parthiban lives a peaceful life with his family")
        
class leodas:
    def lead2(loki):
        print("Leodas is a member of drug cartel and he is ruthless and violent")
        
class sathya(parthiban,leodas):
    def display(loki):
        print("Sathya is confused whether parthiban is a loedas or not")

l1=sathya()

l1.lead1()
l1.lead2()



