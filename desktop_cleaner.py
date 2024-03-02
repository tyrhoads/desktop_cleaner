import shutil, os 
from pathlib import  Path

file = open('tester.txt')
content = file.read()
print(content)
file.write("stuff")
content = file.read()
print(content)