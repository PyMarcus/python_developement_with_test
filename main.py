from unittest import TestCase, main


def sum(x: int, y: int) -> int:  # type hint improve in 1 second the time to run
    """
    Function that sum two values and return the result

    Arg:
        - x: value integer
        - y: value integer
    Return:
        - response integer
    """
    return x + y

def evenOrOdd(*args) -> str:
    """
    Function that verify if a number in args is even or odd

    Arg:
        - args: value integer
    Return:
        - response string
    """
    return "odd" if args[0] % 2 != 0 else "even"


class Test(TestCase):
    """
    this class test the sum function
    and valitate your response
    """
    # its the same that assert sum(5, 5) == 10, but, personalizated
    def test_sum(self):
        self.assertEquals(sum(5, 5), 10)  
    
    # ps: the .. in response means passed tests.But, if there is something wrong, so, a F letter be show.
    def test_wrong_sum(self):
        self.assertEquals(sum(5, 4), 9)  

    # its the same that assert 5 + 5 < 12
    def test_sum2(self):
        self.assertLess(sum(5, 5), 12)  

    # its the same that asser 5 + 5 <= 12
    #def test_sum3(self):
        #self.assertLessEquals(sum(5, 5), 12)
    
    # its the same that assert "impar" if x % 2 != 0 else "par"
    def test_evenOrOdd(self):
        self.assertEquals(evenOrOdd(3), "odd")
        
    ### TDD => test driver developement





if __name__ == '__main__':
    main()  # main from unittest
