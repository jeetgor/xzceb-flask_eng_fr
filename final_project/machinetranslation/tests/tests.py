import unittest
from translator import translator_service,english_to_french,french_to_english


class test_translation(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hello')



class test_null(unittest.TestCase): 
    def test1(self): 
        text=input()
        self.assertEqual(english_to_french(text), None)
        self.assertEqual(french_to_english(text), None)

unittest.main()