https://devrockets.ru/2022/06/11/sokety-v-python-chto-voobshhe-takoe-soket/

# Функции

### Общие для клиента и сервера: 

```
    socket() — создать сокет (функция возвращает объект сокета, методы которого реализуют различные системные вызовы сокетов)
    send()   — передать данные
    recv()   — получить данные
    close()  — закрыть соединение
```

### Серверные:

```
    bind()   — привязать сокет к IP-адресу и порту машины
    listen() — просигнализировать о готовности принимать соединения
    accept() — принять запрос на установку соединения
```

### Клиентские:

```
    connect() — установить соединение
```


