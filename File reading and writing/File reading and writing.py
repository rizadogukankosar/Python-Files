# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

# FILE READING AND WRITING


# open file to read an print all file
f = open("file.txt","r")
print(f.read())
f.close()

# open file to read an print 1 character
f = open("file.txt","r")
print(f.read(1))
f.close()

# open file to read an print with line
f = open("file.txt","r")
for line in f:
    print(line)
f.close()

# open file to write and write "How are you" to file 
f = open("file.txt","a")
f.write("How are you")
f.close()


