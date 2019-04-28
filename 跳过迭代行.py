"""dorpwhile的使用"""

from itertools import dropwhile

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line:line.startswith('#'),f):
        print(line)