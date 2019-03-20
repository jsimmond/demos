#!/usr/bin/python
import cgi

form = cgi.FieldStorage()

firstname = form.getvalue('nombre')
age = form.getvalue('edad')

if form.getvalue('leng1'):
	lang_c = 'ON'
else:
	lang_c = 'OFF'

if form.getvalue('leng2'):
	lang_j = 'ON'
else:
	lang_j = 'OFF'

if form.getvalue('leng3'):
	lang_p = 'ON'
else:
	lang_p = 'OFF'

quakes = form.getvalue('temblores')
print quakes
fday = form.getvalue('dias')
print fday

msg = firstname + "\t" + age + "\t" + lang_c + "\t" + lang_j + "\t" + lang_p + "\t" + quakes + "\t" + fday + "\n"

f = open("data.txt","a+")
f.write(msg)
f.close()

print("Content-Type: text/html\n\n")
print("")

print '''<html>
<head>
	<meta charset="utf-8">
</head>
<body>

<h1>Hola '''

print firstname

print '''</h1>

	<p>Tienes '''

print age

print '''a&ntilde;os, y '''

if quakes == "si":
	print "si"
else:
	print "no"

print ''' le tienes miedo a los temblores<p>
</body>
</html>'''
