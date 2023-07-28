from time import sleep
from socket import socket, AF_INET, SOCK_STREAM


while True:
    s = socket(family=AF_INET, type=SOCK_STREAM)

    try:
        print(f'Создан сокет {s}')
        s.connect(('localhost', 7777))

        print('Отправляю сообщение')
        s.sendall("Привет! Скажи пожалуйста сколько время.".encode('utf-8'))

        input_message = s.recv(1024)
        print("Принял сообщение: %s" % input_message.decode('utf-8'))

        s.close()

        sleep(3)

    except KeyboardInterrupt:
        s.close()
    except Exception as error:
        print(f'{error = }')
        s.close()
