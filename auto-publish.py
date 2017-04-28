#!/usr/bin/python

# Copyright (c) 2017 by catpaw<congtaowang>. All Rights Reserved.

import os
import sys

opts = sys.argv[1:]
print opts

os.system("git add .")
os.system("git commit -m %s" % ("Commit."))
os.system("git push -u origin master")
