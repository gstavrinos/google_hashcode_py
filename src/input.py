#!/usr/bin/env python
import os
from problem import Problem

def readFile(input_file):
    src_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.normpath(src_dir + os.sep + os.pardir + os.sep + "data" + os.sep + input_file)
    p = Problem()
    # TODO initialize the problem object's fields
    return  p
