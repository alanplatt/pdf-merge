#!/usr/bin/env python
import os
import sys
import argparse
from pyPdf import PdfFileWriter, PdfFileReader

__author__ = 'Alan Platt'

def append_to_pdf(input,output):
    for page_number in range(input.numPages):
        output.addPage(input.getPage(page_number))

def main():
    parser = argparse.ArgumentParser(description='Merge two pdf files into one')
    parser.add_argument('--file1', help='The first half of the output document)')
    parser.add_argument('--file2', help='The first half of the output document)')
    parser.add_argument('--outfile', help='Merged output file)')
    args=parser.parse_args()

    file1 = args.file1
    file2 = args.file2
    outfile = args.outfile

    for arg in file1, file2, outfile:
        if arg == None:
            parser.print_help()
            sys.exit(1)

    output = PdfFileWriter()
    append_to_pdf(PdfFileReader(open(file1,"rb")),output)
    append_to_pdf(PdfFileReader(open(file2,"rb")),output)
    output.write(open(outfile,"wb"))

    sys.exit(0)

if __name__ == '__main__':
    main()
