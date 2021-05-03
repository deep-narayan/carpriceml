#!C:\Program Files\Python37\Python.exe
print("Content-type:text/html \n")
import cgi


form = cgi.FieldStorage()

name = form.getvalue("data")

print("""
<html>
<body>
<h1>Prediction Value: {}</h1>
</body>
</html>
""".format(name))
