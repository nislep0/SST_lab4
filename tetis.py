#!/usr/bin/env python3
import sys

from tetris.io_layer import FileReader, FileWriter
from tetris.app import run

def main():
	if len(sys.argv) not in (2, 3):
		print("error")
		sys.exit(1)
	input_path = sys.argv[1]
	print_all = False
	if len(sys.argv) == 3:
		if sys.argv[2] == "--all":
			print_all = True
		else:
			print("error")
			sys.exit(1)

	reader = FileReader(input_path)
	writer = FileWriter()
	code = run(reader, writer, print_all)
	sys.exit(code)

if __name__ == "__main__":
	main()
