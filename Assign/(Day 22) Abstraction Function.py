from abc import ABC,abstractmethod

class home1(ABC):
  @abstractmethod
  def room(self):
    print("There are only 5 rooms in the house")

class home2(home1):
  def room(self):
    print("Additional rooms has been added")

h1=home2()
h1.room()
  
