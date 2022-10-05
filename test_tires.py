import unittest

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class Test_carrigan(unittest.TestCase):
    def test_tires_need_service(self):
        array = [0.9,0.2,0,1]

        tires = Carrigan(array)
        self.assertTrue(tires.needs_service())

    def test_tires_dont_need_service(self):
        array = [0.3,0.2,0,0.7]

        tires = Carrigan(array)
        self.assertFalse(tires.needs_service())

class Test_Octoprime(unittest.TestCase):
    def test_tires_need_service(self):
        array = [1,0.5,0.5,1]

        tires = Octoprime(array)
        self.assertTrue(tires.needs_service())

    def test_tires_dont_need_service(self):
        array = [0.5,0.5,0.2,0.7]

        tires = Octoprime(array)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()