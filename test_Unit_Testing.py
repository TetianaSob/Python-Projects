# test_Unit_Testing.py

import unittest

from Unit_Testing import circle_area 
from math import pi

#create a class from the subclass

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi) 
        self.assertAlmostEqual(circle_area(0), 0)    
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)  
    
# self.assertAlmostEqual(circle_area(1), pi) - the assertAlmostEqual method the first value will be the output 
# of the circle area function and the second value will be the correct answe

# the python unittest framework will compaire these 2 values and if they are 
# correct to the 7 dessimal places. It will asume they are equal.

# self.assertAlmostEqual(circle_area(0), 0)- check the function with the cirlce radiaus 0
# and the circle radiaus '2.1'

#if one of these registers fail the python will register the 'F' fail.