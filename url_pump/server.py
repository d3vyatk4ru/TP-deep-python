import socket
from collections import Counter
from typing import Dict
from bs4 import BeautifulSoup
from urllib.request import urlopen

REPLACE_DATA = [
    '\xa0',
    '\u2060',
    '/', '°',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8', 
    '9',
    '-',
    '©',
    ':', 
    ';',
    ',',
    '.',
    '!',
    '?',
    '  ',
    ]

def get_top_count_words(url: str, top: int) -> Dict[str, int]:

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    text = soup.get_text().lower()

    for sym in REPLACE_DATA:
        text = text.replace(sym, ' ')

    c = Counter(text.split(' '))

    return c[:top]


def server(port: int = 15_000):
    """ Server """

    sock = socket.socket()

    sock.bind(('', port))
    sock.listen(5)

    while True:
        client, _ = sock.accept()

        data = client.recv(4096)

        client.send(data)

if __name__ == "__main__":

    server()


# import socket
# import threading
# import sys

# sock = socket.socket()
# sock.bind(('', 15_000))
# sock.listen(3)
# conn = []

# def Reciver():
#     while 1:
#         for i in range(len(conn)):
#             try:
#                 data = conn[i].recv(1024)
#                 if data:
#                     print(data.decode())
#             except socket.error as e:
#                 if e.errno == 10053:
#                     conn.pop(i)
#                     print("Подключено пользователй:", len(conn))
#                 else:
#                     raise

# def Sender():
#     while 1:
#         global conn
#         message = input()
#         if message:
#             for i in range(len(conn)):
#                 conn[i].send(message.encode())

# def Accepter():
#     while 1:
#         global conn
#         conn.append(sock.accept()[0])
#         print("Подключено пользователй:", len(conn))


# # init threads
# t1 = threading.Thread(target=Reciver)
# t2 = threading.Thread(target=Sender)
# t3 = threading.Thread(target=Accepter)

# # start threads
# t1.start()
# t2.start()
# t3.start()