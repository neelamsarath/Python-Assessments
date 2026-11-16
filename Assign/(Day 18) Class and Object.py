
class wireframe:

    def setdesign(des):
        des.name=input("Enter name of the website: ")
        des.pages=int(input("Enter no.of Pages: "))
        des.buttons=int(input("Enter no.of Buttons: "))

    def getdesign(des):
        print("Webiste name:",des.name,"Pages:",des.pages ,"Buttons:",des.buttons)

d1=wireframe()
d1.setdesign()
d1.getdesign()
'''

class Wireframe:

    def __init__(self, app_name, pages, buttons):
        self.app_name = app_name
        self.pages = pages
        self.buttons = buttons

    def display_wireframe(self):
        print("Application Name:", self.app_name)
        print("Number of Pages:", self.pages)
        print("Number of Buttons:", self.buttons)


# Creating a wireframe
w1 = Wireframe("Shopping Website", 5, 10)

# Creating the deployed application (object)
class Application:

    def __init__(self, wireframe):
        self.name = wireframe.app_name
        self.pages = wireframe.pages
        self.buttons = wireframe.buttons
        self.status = "Deployed"

    def display_application(self):
        print("\n--- Application Details ---")
        print("Application:", self.name)
        print("Pages:", self.pages)
        print("Buttons:", self.buttons)
        print("Status:", self.status)


# Creating application object using wireframe
app1 = Application(w1)

# Displaying details
print("--- Wireframe Details ---")
w1.display_wireframe()

app1.display_application()

'''
        
