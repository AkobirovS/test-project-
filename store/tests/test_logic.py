from django.test import TestCase
from store.logic import ogeratins

class LogicTests(TestCase):
    def test_pulse(self):
        result = ogeratins(13,4,"+")
        self.assertEqual(result,17)
    def test_music(self):
        result = ogeratins(10,9,'-')
        self.assertEqual(result,1)
