#!/usr/bin/python
import time
import commands
import os
str1=raw_input("enter dir name")
t = commands.getoutput("find / -type d -name "+" "+ str1)
if t != '' :
    print t
    str2 = raw_input("enter file to search")
    cur_dir = t

    while True:
      file_list = os.listdir(cur_dir)
      if str2 in file_list:
        print "File Exists in: ", cur_dir
        break
      else:
        print "File not found"
        break
        
else :
    os.system("mkdir /root/Desktop/"+str1)
    print "Directory created"

time.sleep(10)
   




