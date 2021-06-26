import unittest
from dice_roller import DiceRoller as dr

class TestDiceRoller(unittest.TestCase):

    def setUp(self):
        self.number = 0
        self.two_sided_result = dr.two_sided_roll()
        self.four_sided_result = dr.four_sided_roll()
        self.six_sided_result = dr.six_sided_roll()
        self.ten_sided_result = dr.ten_sided_roll()
        self.twelve_sided_result = dr.twelve_sided_roll()
        self.twenty_sided_reult = dr.twenty_sided_roll()

    def test_two_sided(self):
        for number in range(1, 3):
            if(number == self.two_sided_result):
                self.number = number
        self.assertEquals(self.number, self.two_sided_result)
    
    def test_four_sided(self):
        for number in range(1, 5):
            if(number == self.four_sided_result):
                self.number = number
        self.assertEquals(self.number, self.four_sided_result)
    
    def test_six_sided(self):
        for number in range(1, 7):
            if(number == self.six_sided_result):
                self.number = number
        self.assertEquals(self.number, self.six_sided_result)

    def test_ten_sided(self):
        for number in range(1, 11):
            if(number == self.ten_sided_result):
                self.number = number
        self.assertEquals(self.number, self.ten_sided_result)

    def test_twelve_sided(self):
        for number in range(1, 12):
            if(number == self.twelve_sided_result):
                self.number = number
        self.assertEquals(self.number, self.twelve_sided_result)

    def test_twenty_sided(self):
        for number in range(1, 20):
            if(number == self.twenty_sided_reult):
                self.number = number
        self.assertEquals(self.number, self.twenty_sided_reult)

if __name__ == '__main__':
    unittest.main()
