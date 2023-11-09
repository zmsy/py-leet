import unittest

from py_leet.time_based_key_value_store import TimeMap

class TestTimeMap(unittest.TestCase):
    def test1(self):
        """
        Test the basic operations from the example.
        """
        map = TimeMap()
        map.set("foo", "bar", 1)
        self.assertEqual(map.get("foo", 1), "bar")
        self.assertEqual(map.get("foo", 3), "bar")
        map.set("foo", "bar2", 4)
        self.assertEqual(map.get("foo", 4), "bar2")
        self.assertEqual(map.get("foo", 5), "bar2")
