#!/usr/bin/env python

# Builds a cache.manifest file from files in the same directory

import os

cm = "CACHE MANIFEST\n\n# Generated by cm.py\n\n"

nested_dir = 'photo'

for f in os.listdir(os.curdir):
  # if not a hidden file or this file
  if (os.path.isfile(f) and f[0] != "." and f != "cm.py" and f != "cache.manifest" and f != "README"):
    cm += f + "\n"
  # nested images
  elif (os.path.isdir(f) and f == nested_dir):
    for sub_dir in os.listdir(f):
      for f2 in os.listdir(os.path.join(f, sub_dir)):
        (key, ext) = os.path.splitext(os.path.basename(f2))
        cm += os.path.join(f, sub_dir, f2) + "\n"
        cm += sub_dir[:-1] + ".html?" + sub_dir[:-1] + "=" + key + "\n"
  elif (os.path.isdir(f) and f[0] != "."):
    for f2 in os.listdir(f):
      cm += os.path.join(f, f2) + "\n"
      
cm += "\nNETWORK:\n*\n"

f = open('cache.manifest', 'w')
f.write(cm)
f.close()