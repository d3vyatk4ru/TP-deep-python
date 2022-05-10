import unittest
import threading
import time
from server import Server, get_top_count_words
from client import Client


class TestClientServer(unittest.TestCase):

    def test_url_parser(self):

        url = 'https://edition.cnn.com/'

        res = get_top_count_words(url, 3)

        self.assertEqual('{"news": 5, "cnn": 4, "and": 3}', res)

    def test_start_server_client(self):

        urls = [
            'https://edition.cnn.com/',
            'https://drive.google.com',
        ]

        server = Server(7, 15_000, 5)
        server.start_master()
        time.sleep(1)

        client = Client(urls, 15_000, 5)
        client.start_dump()

        time.sleep(1)
        server.stop()


if __name__ == "__main__":
    unittest.main()
