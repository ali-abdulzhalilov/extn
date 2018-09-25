import os
import argparse
	
def extn(filename):
	parts = filename.split('.')
	if len(parts) == 1:
		return None
	else:
		return parts[len(parts)-1]
	
def create_parser():
	parser = argparse.ArgumentParser(prog='extn', add_help=False)
	parser.add_argument('filename', type=str)
	
	return parser
	
def main():
	parser = create_parser()
	args = parser.parse_args()
	print(extn(args.filename))
	
if __name__ == '__main__':
	main()