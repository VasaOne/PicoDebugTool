import keyboard
import helpDoc



def keyboardCheck() :
    if keyboard.read_key() == "h":
        helpDoc.docExplain()
        return True
    elif keyboard.read_key() == "q":
        return False

if __name__ == '__main__':
    next = True
    while next:
        try:
            next = keyboardCheck()
        except:
            print("a error has occured")
