import asyncio 
import sys, os

sys.path.insert(1,os.path.join(os.path.dirname(__file__), 'moduleUsed'))

import moduleUsed.keyboardManager as kbManager
import moduleUsed.serialRead as srlReader



def main():
    ser = srlReader.comInit("/dev/ttyUSB0", 9600)
    nextStep = True
    while nextStep :
        nextStep = kbManager.keyboardCheck()
        srlReader.isReceived(ser)
    ser.close()


if __name__ == "__main__" :
    main()

            


        

