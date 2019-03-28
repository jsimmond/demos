#!/usr/bin/python
import cgi

form = cgi.FieldStorage()

test = form.getvalue('clientName')
test2 = form.getvalue('sub0')

print("Content-Type: text/html\n\n")
print("")

print '''<html>
<head>
	<meta charset="utf-8">
</head>
<body>

<h1>Hola '''

print test
print test2

print '''</h1>
</body>
</html>'''
