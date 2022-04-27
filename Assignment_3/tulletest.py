from threading import Timer

def printHei():
    print('Heisann')
    Timer(2, printHei).start()

printHei()