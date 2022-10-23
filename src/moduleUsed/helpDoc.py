import time

def startDoc():
    print("|-----------debug doc-----------|")
    time.sleep(0.2)
    print("|                               |")


def endDoc():
    print("|                               |")
    time.sleep(0.2)
    print("|-------------------------------|")

def qDoc():
    print("|---------                      |")
    print("|press q :                      |")
    time.sleep(0.2)
    print("|  |-> to quit the debug cession|")
    time.sleep(0.2)
    print("|---------                      |")

def hDoc():
    print("|---------                      |")
    print("|press h :                      |")
    time.sleep(0.2)
    print("|  |-> to have help             |")
    time.sleep(0.2)
    print("|---------                      |")

def iDoc():
    print("|---------                      |")
    print("|press i :                      |")
    time.sleep(0.2)
    print("|  |-> to get serial com info   |")
    time.sleep(0.2)
    print("|---------                      |")


def docExplain():
    startDoc()
    hDoc()
    qDoc()
    iDoc()
    endDoc()

if __name__ == "__main__":
    docExplain()

