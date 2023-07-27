from socket import *
from time import sleep

while True:
    sleep(0.5)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 7777))
    tm = s.recv(1024)
    sleep(0.5)
    s.close()
    print("Текущее время: %s" % tm.decode('utf-8'))

