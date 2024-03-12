def SayHello():
    print("Hello World")

def SayBye():
    print("Bye World")

SayHello()

if(__name__=="__main__"):
    print("Main")
else:
    print(__name__)

SayBye()