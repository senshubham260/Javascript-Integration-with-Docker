#!/usr/bin/python3

print("content-type: text/html")
print()

print('''<style>
pre{
  background color: red;
  color: black;
  font-weight: bold;
  font-size: 20px;
}
</style>
''')
import subprocess as sp
import cgi

fs = cgi.FieldStorage()

cmd = fs.getvalue("x")
output = sp.getoutput(cmd)
#a = "sudo docker ps"
#output = sp.getoutput("docker ps")
print("<body style='padding: 50px;'>")
print('<h1 style="color:#df405a;" >Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")
