f = open('/etc/passwd','r')
for chunks in iter(lambda :f.readlines(),''):
    print(chunks)