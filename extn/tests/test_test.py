from unittest import TestCase

import extn

class TestTest(TestCase):
	def test_is_string(self):
		s = extn.test()
		self.assertTrue(isinstance(s, str))