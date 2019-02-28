#!/usr/bin/env python
import sys

from datetime import datetime

from input import readFile
from problem import Problem
from output import writeResults, prepareResults
from processing import processData

def init():
    if len(sys.argv) == 3:

        input_file = sys.argv[1]
        starttime = datetime.now().strftime("%H-%M-%S")

        prepareResults(starttime, input_file)

        problem = readFile(input_file)

        results = processData(problem, int(sys.argv[2]))

        writeResults(starttime, input_file, results)

    elif len(sys.argv) < 3:
        print "\033[91mNot enough args\033[0m"
    else:
        print "\033[91mToo many args\033[0m"


if __name__ == '__main__':
    init()
