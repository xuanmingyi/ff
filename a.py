#!/usr/bin/env python
import sys

if len(sys.argv) <= 1:
    exit(1)


if sys.argv[1] == "init":
    from init import init
    init()
elif sys.argv[1] == "image":
    from image import Image
    i = Image()
    if sys.argv[2] == "list":
        i.list()
    if sys.argv[2] == "add":
        i.add(sys.argv[3], sys.argv[4])
    if sys.argv[2] == "rm":
        i.rm(sys.argv[3])
elif sys.argv[1] == "network":
    from network import Network
    i = Network()
    if sys.argv[2] == "list":
        i.list()
    if sys.argv[2] == "add":
        i.add(sys.argv[3], sys.argv[4])
    if sys.argv[2] == "rm":
        i.rm(sys.argv[3])
