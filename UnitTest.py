import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        self.testCases = {
            1: {'s1': "this apple is sweet", 's2': "this apple is sour", 'output': ["sweet","sour"]},
            2: {'s1': "apple apple", 's2': "banana", 'output': ["banana"]}
        }
        return super().setUp()
    
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.uncommonFromSentences(case['s1'], case['s2'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.uncommonFromSentences(case['s1'], case['s2'])
            self.assertEqual(res, case['output'])
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    unittest.main()