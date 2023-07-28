import time
from socket import socket, AF_INET, SOCK_STREAM


s = socket(family=AF_INET, type=SOCK_STREAM)
s.bind(('', 7777))
s.listen(3)

host = s.getsockname()


try:
    while True:
        print(f'{host} ожидает подключений')

        client_connection, client_address = s.accept()
        print(f'{client_connection = }')
        print(f"Соединение: {client_connection} с адресом: {client_address}")

        message = client_connection.recv(1024)
        print("Принял сообщение: %s" % message.decode('utf-8'))

        timestr = time.ctime(time.time()) + "\n"
        send_message = f"Текущее время: {timestr}"
        print(f"отправляю сообщение: {send_message}")
        client_connection.sendall(send_message.encode('utf-8'))

        client_connection.close()
        print("Закрыл клиентский сокет")

except KeyboardInterrupt:
    s.close()
except Exception as error:
    print(f'{error = }')
    s.close()


