#! python3
# coding: utf-8
"""
Test tree constructor.
"""
import os
import datetime

poss_dirs = ['spam', 'egg', 'chips', 'mushrooms']
MAX_DEPTH=6

def mkdirs(indir="test_tree", depth=0):
    """ Make the directories. """
    depth+=1

    if depth > MAX_DEPTH:
        return
    os.chdir(indir)
    for d in poss_dirs:
        os.mkdir(d)
        mkdirs(d, depth)
    os.chdir('..')

if __name__ == "__main__":
    started = datetime.datetime.now()
    print("Constructing Test Tree")
    os.mkdir('test_tree')
    mkdirs()
    print(f"Test Tree Constructed in {datetime.datetime.now()-started}")
