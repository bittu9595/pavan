#!/usr/bin/python
import time
import os
str=raw_input("enter dir name")
t=os.system("find / -type d -name %s" %str)
print t
time.sleep(10)
   




