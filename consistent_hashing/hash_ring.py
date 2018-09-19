#
# gino created on 2018/9/18

import hashlib
import random
import string

import numpy as np


class HashRing(object):
    def __init__(self, nodes=None, replicas=3):
        """Manages a hash ring.
        `nodes` is a list of objects that have a proper __str__ representation.
        `replicas` indicates how many virtual points should be used pr. node,
        replicas are required to improve the distribution.
        """
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """Adds a `node` to the hash ring (including a number of replicas).
        """
        for i in range(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            self.ring[key] = node
            self._sorted_keys.append(key)
        self._sorted_keys.sort()

    def remove_node(self, node):
        """Removes `node` from the hash ring and its replicas.
        """
        for i in range(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned.
        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.
        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node], i
        return self.ring[nodes[0]], 0

    def get_nodes(self, string_key):
        """Given a string key it returns the nodes as a generator that can hold the key.
        The generator is never ending and iterates through the ring
        starting at the correct position.
        """
        if not self.ring:
            yield None, None
        node, pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]
        while True:
            for key in self._sorted_keys:
                yield self.ring[key]

    def gen_key(self, key):
        """Given a string key it returns a long value,
        this long value represents a place on the hash ring.
        md5 is currently used because it mixes well.
        """
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)

    def generate_data(self, length, size):
        """
        generate data for test
        :param length:  length of one word
        :param size: data size
        :return: data
        """
        return [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)) for _ in range(size)]


# test code
if __name__ == '__main__':
    ring = HashRing()

    # add nodes
    ring.add_node("192.168.1.1")
    ring.add_node("192.168.1.2")
    ring.add_node("192.168.1.3")

    # check load variance, small is better
    # total always equals 2**32
    total = 0
    diffs = []
    for i in range(len(ring._sorted_keys)):
        if i + 1 != len(ring._sorted_keys):
            diff = ring._sorted_keys[i + 1] - ring._sorted_keys[i]
            diffs.append(diff)
            print(diff)
            total += diff
        else:
            diff = 2 ** 32 - ring._sorted_keys[i] + ring._sorted_keys[0]
            diffs.append(diff)
            print(diff)
            total += diff
    print("total:{}".format(total))
    print("variance:{}".format(int(np.var(diffs))))
    print("\n")

    # generate data for simulating
    data = ring.generate_data(8, 8)
    for item in data:
        print(item)
        print(ring.get_node(item))
        print(ring.get_node_pos(item))
        print("\n")
