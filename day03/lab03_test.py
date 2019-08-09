import unittest
from lab03_Crystal import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        self.assertEqual(YELL, shout("yell"))
        with self.assertRaises(TypeError):shout(5)
    
    #def test_reverse(self):

    #def test_reversewords(self):

    #def test_reversewordletters(self):

    #def test_piglatin(self):


if __name__ == '__main__':
  unittest.main()



def test_vowels(self):
    self.assertEqual(4, count_vowels("mississippi"))
    with self.assertRaises(TypeError): count_vowels(5)