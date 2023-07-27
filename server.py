from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(1)


while True:
    client, addr = s.accept()
    print(client)
    print("Получен запрос на соединение от %s" % str(addr))

    timestr = time.ctime(time.time()) + "\n"
    client.send(timestr.encode('utf-8'))
    client.close()

