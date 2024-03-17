'''
python
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.>>> f=open("01_.py")
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'\n'
>>> f.readline()
'username="cmrohityadav"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''  
>>> f.readline()
''  
>>> f.readline()
''
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> f=open("01_.py")
>>> f.__next__()     
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'username="cmrohityadav"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for line in open("01_.py"):
...     print(line)
... 
import time



print("chai is here")



username="cmrohityadav"

print(username)
>>> f=open("01_.py")
>>> while True:
...     line=f.readline()
...     if not line: break
...     print(line,end="")
... 
import time

print("chai is here")

username="cmrohityadav"
print(username)>>>
'''

'''
test="rohit"
>>> if not test:
...     print("chai")
... 
>>> 
>>> test=""
>>> if not test:
...     print("chai")
... 
chai 
'''