import sys
import serial



def comInit(serialPath, baud):
    ser = serial.Serial(serialPath, baud, timeout=1)
    print("com initialisation done for port: " + serialPath)
    print(ser.is_open)
    return ser


def isReceived(ser):
    if(ser.is_open):
        reader = ser.readline()
        if (reader != b''):
            print(reader)
            return True
        else :
            return False
    else:
        print("serial port not open")
        return False


if __name__ == "__main__":
    ser = comInit("/dev/ttyUSB0", 9600)
    next = True
    while next:
        if (isReceived(ser)):
            print("received!")
            next = True

    ser.close()

