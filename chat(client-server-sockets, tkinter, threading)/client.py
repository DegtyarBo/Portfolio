from socket import socket
from threading import Thread


def client(correct= '', obj={}):
        addres = ('127.0.0.1', 8000)

        def reader(s):
                while True:
                        data = s.recv(100000)
                        if not data:
                                break
                        print('Chat Message:' + data.decode())

        with socket() as s:
                s.connect(addres)
                t = Thread(target=reader, args = [s])
                t.start()
                # создаем функцию, которая будет вызываться и главного кода, но будет знать о
                # клиенте, значит, сможет считывать текст из чата
                def flag(msg):
                        msg = msg.encode()
                        s.sendall(msg)

                obj['flag'] = flag
                t.join()
