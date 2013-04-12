class fakemodule:
    @staticmethod
    def fun():
        return 'fake'

import sys
sys.modules['mymodule'] = fakemodule

import unittest
import hello

class Test(unittest.TestCase):


    def testName(self):
        self.assertEqual('fake', hello.get_mymodule_fun())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()