#!/usr/bin/python

# Copyright (c) 2017 by catpaw<congtaowang>. All Rights Reserved.

import os
import sys

opts = sys.argv[1:]
print opts

def descinfo():
 try:
  opts = sys.argv[1:]
  if len(opts) == 0:
   return 'Commit.'
  else:
   if opts.contains('-i'):
    val = opts[opts.indexOf('-i')+1]
    if val == None or val == '':
     return 'Commit.'
    return val
 except Exception, msg:
  print msg
  return 'Commit.'

os.system("git add .")
os.system("git commit -m %s" % (descinfo()))
os.system("git push -u origin master")
