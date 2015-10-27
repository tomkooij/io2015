# unittest for 2187

import unittest
from board import Bord

class MergeRowLeft(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Bord._mergerow([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(Bord._mergerow([0, 1, 0, 0]), [1, 0, 0, 0])
        self.assertEqual(Bord._mergerow([0, 0, 1, 1]), [2, 0, 0, 0])
        self.assertEqual(Bord._mergerow([0, 1, 1, 1]), [2, 1, 0, 0])
        self.assertEqual(Bord._mergerow([1, 0, 0, 1]), [2, 0, 0, 0])
        self.assertEqual(Bord._mergerow([0, 1, 0, 1]), [2, 0, 0, 0])
        self.assertEqual(Bord._mergerow([1, 1, 1, 1]), [2, 2, 0, 0])
        self.assertEqual(Bord._mergerow([1, 4, 4, 1]), [1, 5, 1, 0])
        self.assertEqual(Bord._mergerow([2, -1, 1, 1]), [2, 1, 0, 0])
        self.assertEqual(Bord._mergerow([1, -1, 1, 3]), [1, 3, 0, 0])
        self.assertEqual(Bord._mergerow([5, -1, 1, 0]), [5, 0, 0, 0])

class MergeRowRight(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Bord._mergerow([0, 0, 0, 0], left=False), [0, 0, 0, 0])
        self.assertEqual(Bord._mergerow([0, 1, 0, 1], left=False), [0, 0, 0, 2])
        self.assertEqual(Bord._mergerow([1, 0, 0, 0], left=False), [0, 0, 0, 1])
        self.assertEqual(Bord._mergerow([0, 0, 1, 1], left=False), [0, 0, 0, 2])
        self.assertEqual(Bord._mergerow([-1, 0, 0, -1], left=False), [0, 0, 0, -2])
        self.assertEqual(Bord._mergerow([1, -1, 1, 3], left=False), [0, 0, 1, 3])
        self.assertEqual(Bord._mergerow([-1, 1, 1, 0], left=False), [0, 0, -1, 2])


class MergeDestroySimilar(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Bord._mergerow([0, -2, 2, 0]), [0, 0, 0, 0])
        self.assertEqual(Bord._mergerow([2, -5, 0, 5]), [2, 0, 0, 0])
