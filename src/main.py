from metadata.python.caper_runner import CaperRunner

import argparse
import sys

def GetCaperArgParser():
    """ Return the Caper CLI Argu Parser """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action='store', help='Filename to collect metadata from')
    parser.add_argument('-l', '--line', action='store', type=int, help='The line number of the function to collect metadata from. 1 is the first line of the file.')
    parser.add_argument('-e', '--exe', action='store', help='The executable to use to run the caper file.')
    return parser

def main(args):
    """ Run the main file """
    parser = GetCaperArgParser()
    arguments = parser.parse_args(args)
    runner = CaperRunner(arguments.filename, arguments.line, arguments.exe)
    runner.run()
    

if __name__ == "__main__":
    main(sys.argv[1:])