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
			
	def test_with_too_much_args(self):
		with self.assertRaises(SystemExit):
			self.parser.parse_args(['first_arg', 'second_arg'])
			
	def test_no_extension(self):
		args = self.parser.parse_args(['some_file'])
		result = extn(args.filename)
		self.assertEqual(result, None)
	
	def test_some_extension(self):
		args = self.parser.parse_args(['some_file.txt'])
		result = extn(args.filename)
		self.assertEqual(result, 'txt')