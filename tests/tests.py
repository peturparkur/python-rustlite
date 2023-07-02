import unittest
import iterlite.enumerable as itl

class TestIteration(unittest.TestCase):

    def test_map(self):
        predicted = itl.Iter(range(1000)).map(lambda x: x ** 2)
        answer = map(lambda x: x**2, range(1000))
        for p, a, in zip(predicted, answer):
            self.assertEqual(p, a)
    
    def test_groupby(self):
        grouped = itl.Iter(range(1000)).group_by(lambda x: x // 10)
        self.assertEqual(grouped.count(), 100)
        for x, a in zip(grouped.map(lambda k, _: k), range(100)):
            self.assertEqual(x, a)
        
        for left, right in zip(grouped.map(lambda _, grp: grp), [range(10) for i in range(100)]):
            for x, a in zip(left, right):
                self.assertEqual(x, a)

        

if __name__ == '__main__':
    unittest.main()