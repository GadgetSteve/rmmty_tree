#! python3

"""
rmmpty_tree.py is intended to traverse a directory tree and remove all of the empty directories.
Author: Steve Barnes

"""

import os
import sys
import argparse
import pathlib
import datetime
import time

def parse_args(argv: dict):
    """ Parse the arguments."""
    parser = argparse.ArgumentParser(
        prog="rmmpty_tree", usage="rmmpty_tree start_dir [...]", description="Remove empty directory trees", add_help="True",
        epilog="If a warning of possible long path problems is shown an no deletions happen try with shorter path(s)"
    )
    parser.add_argument("start_dir", nargs='+', help="Directory that you wish to processes, more than one may be given")
    return parser.parse_args(argv)

def pass_rmmt(adir: str, start_count: int=0) -> int:
    """ Traverse the directory tree removing empty ones."""
    count = 0
    if not os.path.exists(adir):
        print(f"\r{adir} doesn't exist", end="")
        return 0
    for root, dirs, files in os.walk(adir, topdown=False, followlinks=False):
        #print(f"{root=}  {len(dirs)=} {len(files)=}")
        if len(dirs) + len(files) == 0:
            os.rmdir(root)
            time.sleep(0.001)
            count += 1
            if count % 100 == 0:
                print(f"\rDeleted {count+start_count}", end='')
        elif files:
            print(f"\n{root}: and acestors left as has {len(files)} files")
            time.sleep(0.001)
        #else:
        #    print(f"{root=} {len(dirs)=}")
    #else:
    #    print("No Walk!")
    return count


def rmmt(start_dir: str) -> int:
    """ Traverse the directory tree removing empty ones in multiple passes."""
    total = 0
    adir = pathlib.Path(start_dir)
    print("Processing", adir)
    if len(start_dir) > 100:
        print("Possible Long Path Problem!")
    while deleted := pass_rmmt(adir, total):
        total += deleted
    print("\r", total, "empty directories removed")
    return total

if __name__ == "__main__":
    ST = datetime.datetime.now()
    if getattr(sys, "frozen", False):
        ARGS = parse_args(sys.argv[1:])
    else:
        ARGS = parse_args(sys.argv[1:])
        
    total = sum([rmmt(sd) for sd in ARGS.start_dir])
    ET = datetime.datetime.now()
    print(total, "Empty Directories Removed in", ET-ST)
    
