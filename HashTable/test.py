import unittest

from hashtable import HashTable


class HashTableTest(unittest.TestCase):
    def testSetGet(self):
        h = HashTable()

        # Basic set and get operation
        h.set('a', 2)
        h.set('b', 5)
        self.assertEqual(h.get('a'), 2)
        self.assertEqual(h.get('b'), 5)

        # Set update operation
        h.set('a', 3)
        self.assertEqual(h.get('a'), 3)

    def testBadGet(self):
        h = HashTable()

        self.assertEqual(h.get('a'), -1)

    def testRemove(self):
        h = HashTable()

        h.set('a', 1)
        h.remove('a')
        self.assertEqual(h.get('a'), -1)

    def testBadRemove(self):
        h = HashTable()

        self.assertRaises(KeyError, h.remove, 'a')


if __name__ == '__main__':
    unittest.main()
