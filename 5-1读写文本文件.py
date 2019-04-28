with open('/etc/passwd','r',newline='') as f:  # newline 处理换行符
    for line in f:
        print(line)
