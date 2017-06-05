#!/usr/bin/python
import time
a=raw_input("enter first input")
b=raw_input("enter second input")
if a.isdigit() and b.isdigit() :
   print int(a)+int(b)
elif a.isdigit() or b.isdigit() :
   print "alpha numeric"
else :
   print a+" "+b
time.sleep(15)

