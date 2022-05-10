import socket
import json
from typing import List
import threading

import click

# pylint: disable= E1120


class Client:

    def __init__(self, urls: List[str] = None, port: int = 15_000,
                 n_threads: int = 5) -> None:
        self.urls = urls
        self.port = port
        self.n_threads = n_threads

    @staticmethod
    def separate_url(urls: List[str], n_threads: int) -> List[List[str]]:

        n_urls = len(urls) / n_threads

        n_urls = int(n_urls) + 1 if len(urls) % n_threads else int(n_urls)

        return [
            urls[n_urls * start:n_urls * (start + 1)]
            for start in range(n_threads)
        ]

    def _worker(self, part_url: List[List[str]]) -> None:

        for url in part_url:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', self.port))

            sock.send(url.encode())
            data = sock.recv(4096)

            print(f'{url}: ', data.decode())
            sock.close()

    def start_dump(self) -> None:

        separated_url = self.separate_url(self.urls, self.n_threads)

        threads = [
            threading.Thread(target=self._worker, args=(part_url,))
            for part_url in separated_url
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


@click.command(name='client_start')
@click.argument('n_threads', default=5)
@click.argument('data_path', default='url.json')
def client_start_command(data_path: str, n_threads: int):

    with open(data_path, 'r', encoding='utf-8') as json_file:
        urls: List[str] = json.load(json_file)

    print('file: ', data_path)
    print('n_threds: ', n_threads)

    client = Client(urls, 15_000, n_threads)
    client.start_dump()


if __name__ == '__main__':

    client_start_command()
