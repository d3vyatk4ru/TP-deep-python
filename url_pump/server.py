import socket
from collections import Counter
from typing import Dict
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import click
import threading
import time

REPLACE_DATA = [
    '\xa0',
    '\u2060',
    '\n',
    '\r',
    '\t',
    '/',
    '°',
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
    '|',
    '—',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '\\',
    '*',
    '+',
    '=',
    '&',
    ]


def get_top_count_words(url: str, top: int) -> str:

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    text = soup.get_text().lower()

    for sym in REPLACE_DATA:
        text = text.replace(sym, ' ')

    c = dict(Counter(text.split(' ')))

    try:
        del c['']
    except KeyError:
        pass
    
    c = dict(sorted(c.items(), key = lambda x: x[1], reverse=True)[:top])

    json_data = json.dumps(c, ensure_ascii=False)

    return json_data


class Server:

    def __init__(self, top_words: int, port: int = 15_000, n_workers: int=5) -> None:
        self.n_workers = n_workers
        self.top_word = top_words
        self.lock = threading.Lock()
        self.port = port
        self.n_processed_urls = 0
        self.num_threads = 0

    def start_master(self) -> None:
        serv = threading.Thread(target=self.server, daemon=True)
        serv.start()

    def server(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', self.port))

        print(f'Server listening on port: {self.port}')
        self.sock.listen(1000)

        self.n_processed_urls = 0
        self.num_threads = 0

        while True:

            client, _ = self.sock.accept()

            data = client.recv(4096)

            while self.num_threads >= self.n_workers:
                continue

            with self.lock:
                self.num_threads += 1
            
            thread = threading.Thread(
                target=self.workers,
                args=(data.decode(),
                self.top_word,
                client)
            )

            thread.start()

    def workers(self, url, top_word, client):
        json_response = get_top_count_words(url, top_word)

        client.send(json_response.encode())
        client.close()

        with self.lock:
            self.num_threads -= 1
            self.n_processed_urls += 1
            print(f'n_urls: {self.n_processed_urls}')

    def stop(self) -> None:
        self.sock.close()


@click.command(name='server_start')
@click.argument('n_workers', default=5)
@click.argument('top_words', default=3)
def start_server_command(n_workers: int, top_words: int):
    
    server = Server(top_words, 15_000, n_workers)

    server.start_master()

    time.sleep(2)

    while True:
        time.sleep(1)


if __name__ == "__main__":

    # start_server_command()

    url = "https://edition.cnn.com/"

    res = get_top_count_words(url, 3)

    print(res)