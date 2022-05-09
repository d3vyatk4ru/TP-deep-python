

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

        self.limit = limit

    def get(self, key) -> object:
        '''
        Args:
            key: hashable - key to value in cache
        '''

        if key not in self.cache:
            return None

        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        self.__move2head(node)

        return node.val

    def set(self, key, val) -> bool:

        if key in self.cache:
            self.cache[key].val = val
            self.__move2head(self.cache[key])
            return True

        if len(self.cache) == self.limit:
            self.__delete_node(self.tail.prev)

        node = Node(key, val)
        self.cache[key] = node
        self.__move2head(node)

        return True

    def __move2head(self, node: Node) -> None:
        ''' Move to head incoming node '''
        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    def __delete_node(self, node: Node) -> None:
        ''' Delete last node '''
        self.tail.prev = node.prev
        node.prev.next = self.tail

        del self.cache[node.key]

    def __str__(self) -> str:
        ''' String visualization LRU cache '''

        node = self.head
        visual = ''

        for _ in enumerate(self.cache):
            node = node.next
            visual += f' -> {str(node)}'

        return f'{visual} ->'
