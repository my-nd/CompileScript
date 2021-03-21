#!/usr/bin/env python3.9

"""
The goal of this script is to compile and run programs faster

1-Checks the file extension to determine its type
2-Compile the program
3-Execute the program
"""

import sys
import os
import subprocess

if len(sys.argv) == 1:
    print("No program to compile.")
    exit(1)
elif len(sys.argv) > 2:
    print("Can only compile one program.")
    exit(1)

sourceName = sys.argv[1]
base = os.path.splitext(sourceName)[0]
ext = os.path.splitext(sourceName)[1]

if ext == ".c":
    gcc = ["gcc", "-Wall", "-g", sourceName, "-o", base]

    # Create pipe, execute gcc and wait for it to end
    subP = subprocess.Popen(gcc)
    subP.wait()

    # Execute the compiled program
    subprocess.call(["./"+base])

elif ext == ".java":
    # Create pipe, execute gcc and wait for it to end
    subP = subprocess.Popen(["javac", sourceName])
    subP.wait()

    # Execute the compiled program
    subprocess.call(["java", base])

elif ext == ".ml":
    ocamlc = ["ocamlc", sourceName, "-o", base]

    # Create pipe, execute gcc and wait for it to end
    subP = subprocess.Popen(ocamlc)
    subP.wait()

    # Execute the compiled program
    subprocess.call(["./"+base])

else:
    print("Can't compile this program.")



