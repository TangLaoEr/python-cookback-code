#with open('/etc/passwd','r') as f:
#    for line in f:
#        print(line)
#
#

"""

利用itertools.dropwhile指定的部分

"""


from itertools import dropwhile
with open('/etc/passwd','r') as f:
    for line in dropwhile(lambda x:x.startswith('#'),f):
        print(line)
