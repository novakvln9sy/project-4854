# tests/test_basic.py - novakvln9sy/project-4854
import unittest

from utils import chunk, slugify


class TestUtils(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello  World!"), "hello-world")

    def test_chunk(self):
        self.assertEqual(list(chunk([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

    def test_chunk_rejects_zero(self):
        with self.assertRaises(ValueError):
            list(chunk([1], 0))


if __name__ == "__main__":
    unittest.main()


