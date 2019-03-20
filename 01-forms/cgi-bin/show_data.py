#!/usr/bin/python

print("Content-Type: text/html\n\n")
print("")

print '''<html>
<head>
<meta charset="utf-8">
    <title>Datos recolectados</title>
</head>
<body>'''

print '''<table border="1" cellpadding="5">
	<tr><th>Nombre</th>
		<th>Edad</th>
		<th>C</th>
		<th>Java</th>
		<th>Python</th>
		<th>Temblores?</th>
		<th>Dia favorito</th></tr>
'''

f = open("data.txt","r")

for line in f:
	data = line.strip().split()
	print "<tr><td>"
	print '</td><td>'.join(d for d in data) 
	print "</td></tr>"

f.close()

print '''</body>
</html>'''


