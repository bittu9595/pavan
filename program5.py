#!/usr/bin/python
import os
import time
a=raw_input("enter no")
if int(a)==1 :
   print "mozilla"
if int(a)==2 :
   os.system("gnome-session-quit --force")
time.sleep(15)
