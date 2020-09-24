import argparse
import os, time
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mtime", help="last modification time", action="store_true")
parser.add_argument("-s", "--size", help="file's size", action="store_true")
parser.add_argument("-r", "--rename", help="file rename", action="store_true")
args = parser.parse_args()
st = os.stat('/Users/elena/PycharmProjects/sas/arg1.py')
if args.mtime:
    print("last modified: %s" % time.ctime(st.st_mtime))
if args.size:
    print("file size: %s" % (st.st_size / 2**10))
if args.rename:
    os.rename("arg1.py", "arg1.py")

