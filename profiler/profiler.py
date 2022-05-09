""" Study of profiler """

import weakref
import cProfile
import pstats
import io
from memory_profiler import profile

from lru_cache import LRUCache

# pylint: disable= R0903, C0103
#
# R0903: Too few public methods (0/2) (too-few-public-methods)
#
# C0103: Variable name <name> doesn't conform to snake_case naming style

N_VALUE = 500_000


class CarSlots:
    """ Class with slots """

    __slots__ = ['color', 'doors', 'owner']

    def __init__(self, color: str, doors: int, owner: str) -> None:
        self.color = color
        self.doors = doors
        self.owner = owner


class CarOrdinal:
    """ Class without slots """

    def __init__(self, color: str, doors: int, owner: str) -> None:
        self.color = color
        self.doors = doors
        self.owner = owner


@profile
def mem_profile():
    """ Check memory profiler """

    cache_1 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_1.set(key, CarSlots(color='red', doors=5, owner='Daniil'))

    cache_2 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_2.set(key, CarOrdinal(color='red', doors=5, owner='Daniil'))

    obj = CarOrdinal(color='red', doors=5, owner='Daniil')

    cache_3 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_3.set(key,  weakref.ref(obj))


def call_profile():
    """ Check call profiler """

    pr = cProfile.Profile()
    pr.enable()

    cache_1 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_1.set(key, CarSlots(color='red', doors=5, owner='Daniil'))

    cache_2 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_2.set(key, CarOrdinal(color='red', doors=5, owner='Daniil'))

    obj = CarOrdinal(color='red', doors=5, owner='Daniil')

    cache_3 = LRUCache(limit=N_VALUE)

    for key in range(N_VALUE):
        cache_3.set(key, weakref.ref(obj))

    pr.disable()

    out = io.StringIO()

    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()

    print(out.getvalue())


if __name__ == '__main__':

    mem_profile()

    call_profile()
