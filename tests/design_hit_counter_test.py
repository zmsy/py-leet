import unittest
from py_leet.design_hit_counter import HitCounter


class TestDesignHitCounter(unittest.TestCase):
    def test1(self):
        sol = HitCounter()
        sol.hit(1)
        sol.hit(2)
        sol.hit(3)
        self.assertEqual(sol.getHits(4), 3)
        sol.hit(300)
        self.assertEqual(sol.getHits(300), 4)
        self.assertEqual(sol.getHits(301), 3)

    def test2(self):
        sol = HitCounter()
        sol.hit(10)
        sol.hit(20)
        sol.hit(30)
        sol.hit(40)
        sol.hit(50)
        sol.hit(50)
        sol.hit(60)
        sol.hit(70)
        sol.hit(80)
        sol.hit(90)
        sol.hit(100)
        sol.hit(300)
        sol.hit(310)
        sol.hit(320)
        sol.hit(330)
        self.assertEqual(sol.getHits(331), 12)
