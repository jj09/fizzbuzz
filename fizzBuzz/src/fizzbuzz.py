class FizzBuzz(object):
    """
    Program that prints the numbers from 1 to 100. 
    But for multiples of three print 'Fizz' instead of the number 
    and for the multiples of five print 'Buzz'. 
    For numbers which are multiples of both three and five print 'FizzBuzz'.
    """


    def __init__(self):
        """
        Constructor
        """
        
    def get_value(self, number):
        
        if number % 15 == 0:
            return "Fizz Buzz"
        
        if number % 3 == 0:
            return "Fizz"
        
        if number % 5 == 0:
            return "Buzz"
        
        return number
    
    def main(self):
        for number in range(1,100):
            print self.get_value(number)
        
    
if __name__ == "__main__":
    fb = FizzBuzz()
    fb.main()