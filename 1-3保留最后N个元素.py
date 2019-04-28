"""
利用collectins
"""
from collections import deque

def search(lines, pattern, history=5):
    previours_history = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previours_history
        previours_history.append(li)


if __name__ == '__main__':
    with open('/etc/passwd','r') as f:
        for line ,prevalues in search(f,'var'):
            for pline in prevalues:
                print(pline,end=' ')
            print('line:',line,end=' ')
            print('-'*20)