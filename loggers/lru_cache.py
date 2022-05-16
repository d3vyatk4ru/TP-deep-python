import logging
import argparse

CACHE_SIZE = 10

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s %(levelname)-7s: %(message)s',
    handlers=[
        logging.FileHandler('lru_cache.log'),
    ]
)

logger = logging.getLogger('lru_cache')


class Node:
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f'[{str(self.key)}, {str(self.val)}]'

    def __repr__(self) -> str:
        return f'[{str(self.key)}, {str(self.val)}]'


class LRUCache:

    def __init__(self, limit: int = 42) -> None:
        '''
        Args:
            limit: int - max cache size
        '''

        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        if limit < 1:
            logger.error('Cache size must be a positive number')

        self.limit = limit

    def get(self, key) -> object:
        '''
        Args:
            key: hashable - key to value in cache
        '''

        if key not in self.cache:
            logger.warning('Not existing key %s in cache', key)
            return None

        node = self.cache[key]
        logger.info(
            'Was return element %s with key %s',
            node.val,
            key
        )

        node.prev.next = node.next
        node.next.prev = node.prev

        self.__move2head(node)

        return node.val

    def set(self, key, val) -> bool:

        if key in self.cache:
            logger.info(
                'Adding value %s with  key %s already exist in cache',
                val,
                key,
            )
            self.cache[key].val = val
            self.__move2head(self.cache[key])
            return True

        if len(self.cache) == self.limit:
            logger.warning('Cache is full')
            self.__delete_node(self.tail.prev)

        node = Node(key, val)
        self.cache[key] = node
        logger.info(
            'Adding new element %s with key %s in cache',
            node.val,
            key,
        )
        self.__move2head(node)

        return True

    def __move2head(self, node: Node) -> None:
        ''' Move to head incoming node '''

        logger.info(
            'Element %s with key %s move to cache head',
            node.val,
            node.key,
        )

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    def __delete_node(self, node: Node) -> None:
        ''' Delete last node '''
        self.tail.prev = node.prev
        node.prev.next = self.tail

        logger.info('Deleting old element')

        del self.cache[node.key]

    def __str__(self) -> str:
        ''' String visualization LRU cache '''

        node = self.head
        visual = ''

        for _ in enumerate(self.cache):
            node = node.next
            visual += f' -> {str(node)}'

        return f'{visual} ->'


def logger_setting(cond: bool) -> None:

    if cond:
        stdout_log_format = logging.Formatter(
            '[%(asctime)s] [%(threadName)s] (%(name)s): %(message)s'
        )

        cli = logging.StreamHandler()
        cli.setFormatter(stdout_log_format)
        logger.addHandler(cli)


if __name__ == '__main__':
    """ -s is 0 or 1 """

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=int) # 0 or 1

    args = parser.parse_args()

    logger_setting(args.s)

    cache = LRUCache(limit=CACHE_SIZE)

    for i in range(CACHE_SIZE):
        cache.set(i, (i + 1) * str(i))

    cache.get(CACHE_SIZE - 1)
    cache.get(CACHE_SIZE - 2)
    cache.get(CACHE_SIZE - 3)

    for i in range(5):
        cache.set(CACHE_SIZE + i, CACHE_SIZE + i)

    cache.set(CACHE_SIZE + 1, CACHE_SIZE - 1)
