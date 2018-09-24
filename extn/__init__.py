import argparse
	
def extn(args):
	pass
	
def create_parser():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('filenames', nargs='+', type=str, metavar='FILENAME')
	
	return parser
	
def main():
	parser = create_parser()
	args = parser.parse_args()
	extn(args)
	
if __name__ == '__main__':
	main()