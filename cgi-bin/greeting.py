#!/usr/local/bin/python3

import cgi

form = cgi.FieldStorage()

v_name = form.getvalue('name')

print()
print(f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <link rel="stylesheet" href="/style.css">
  </head>
  <body> 
    <h1 style="background-color:Yellow;"> Hello {v_name} </h1>
  </body>
</html>""")
