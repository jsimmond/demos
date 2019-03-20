#!/usr/bin/python
import cgi

form = cgi.FieldStorage()

firstname = form.getvalue('nombre')

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
</body>
</html>'''
