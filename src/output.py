#!/usr/bin/env python
import os
import tarfile

def tarBallSrc(src_dir, dst_dir):
    print "\033[94mCreating tarball...\033[0m"
    tar = tarfile.open("src.tar.gz", "w:gz")
    src_file = os.path.normpath(src_dir + os.sep + "src.tar.gz")
    dst_file = os.path.normpath(dst_dir + os.sep + "src.tar.gz")
    tar.add(src_dir, arcname="src")
    os.rename(src_file, dst_file)
    print "\033[92mTarball was written in {}\033[0m".format(dst_file)

def prepareResults(starttime, input_file):
    src_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.normpath(src_dir + os.sep + os.pardir + os.sep + "results" + os.sep + starttime + "_" + input_file)
    os.mkdir(out_dir)
    tarBallSrc(src_dir, out_dir)

def writeResults(starttime, input_file, results):
    src_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.normpath(src_dir + os.sep + os.pardir + os.sep + "results" + os.sep + starttime + "_" + input_file)
    outfile = os.path.normpath(out_dir + os.sep + "results.txt")
    with open(outfile, 'w') as f:
        f.write("TODO")
