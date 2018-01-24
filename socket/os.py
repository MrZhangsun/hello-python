import os
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print filename, "does not exist"
        exit(0)
    if not os.access(filename, os.R_OK):
        print "access denied."
        exit(0)
    print "Reading info from :", filename
