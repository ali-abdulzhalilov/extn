from unittest import TestCase
from extn import create_parser, extn

class CommandLineTestCase(TestCase):
	"""
	Base TestCase class, sets up a CLI parser
	"""
	@classmethod
	def setUpClass(cls):
		parser = create_parser()
		cls.parser = parser


class ExtnTestCase(CommandLineTestCase):

	def test_with_no_args(self):
		with self.assertRaises(SystemExit):
			self.parser.parse_args([])