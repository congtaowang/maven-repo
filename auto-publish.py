#!/usr/bin/python

# Copyright (c) 2017 by catpaw<congtaowang>. All Rights Reserved.

import os

os.system("git add .")
os.system("git commit -am %s" % ("Commit."))
os.system("git push -u origin master")
