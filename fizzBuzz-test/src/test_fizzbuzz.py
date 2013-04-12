import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    """
    Test cases for FizzBuzz program. 
    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_get_number(self):
        """ 
        some number different than 3 or 5
        """
        
        fb = fizzbuzz.FizzBuzz()
        number = 2
        expected = 2
        result = fb.get_value(number)
        self.assertEqual(expected, result)
        
    
    def test_get_number_returns_fizz(self):
        """"
        Multiple of 3 returns Fizz.
        """ 
        
        fb = fizzbuzz.FizzBuzz()
        number = 3
        expected = "Fizz"
        result = fb.get_value(number)
        self.assertEqual(expected, result)
        
    
    def test_get_number_returns_buzz(self):
        """"
        Multiple of 5 returns Buzz.
        """     
        
        fb = fizzbuzz.FizzBuzz()
        number = 5
        expected = "Buzz"
        result = fb.get_value(number)
        self.assertEqual(expected, result)
        
        
    def test_get_number_returns_fizz_buzz(self):        
        """"
        Multiple of 3 and 5 returns Buzz.
        """     
        
        fb = fizzbuzz.FizzBuzz()
        number = 15
        expected = "Fizz Buzz"
        result = fb.get_value(number)
        self.assertEqual(expected, result)
        
        
    @unittest.skip("showing method skipping")
    def test_sth(self):
        self.assertEqual(4,5)
     


if __name__ == "__main__":
    unittest.main()