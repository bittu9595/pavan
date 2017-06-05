#!/usr/bin/python
import sys
import time
sum=0
x=sys.argv[1:]
for i in x :
  sum=sum+int(i)

print sum
time.sleep(10)
