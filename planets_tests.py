import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("111")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 42.18 pounds.\nOn Jupiter you would weigh 259.74 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_03(self):
        sys.stdin = io.StringIO("184")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 69.92 pounds.\nOn Jupiter you would weigh 430.56 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())



if __name__ == "__main__":
        unittest.main()
