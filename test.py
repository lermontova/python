import unittest
def sl(n1,n2):
    return n1+n2
class TestCase(unittest.TestCase):
    def test_sl_1(self):
        actual=sl(10,1)
        exp=11
        self.assertEqual(actual,exp)
        
    def test_sl_2(self):
        actual=sl(10,5)
        exp=14
        self.assertEqual(actual,exp)
    

if __name__=='__main__':
    unittest.main(exit=False)
