#!/bin/sh
path="/Users/yu/code/git/chinanet"
#python -u aviod output buffering
nohup python -u $path'/chinanet.py' > $path'/chinanet.log' 2>&1 &
