#!/usr/bin/python
import commands 
import sys
import time
x=sys.argv[1:]
for i in x:
    st,output=commands.getstatusoutput(i)
    if(st==0):
      print output
    else:
       print "please enter correct commannd"
