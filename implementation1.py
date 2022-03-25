import sys
from tkinter import Y
ssr = sys.stdin.readline

n = int(ssr())
command = ssr().split()

x,y = 1,1
for i in command:
    if i == 'L':
        if x != 1:
            x -= 1
        else:
            x = x
    elif i == 'R':
        if x != n:
            x += 1
        else:
            x = x
    elif i == 'U':
        if y != 1:
            y += 1
        else:
            y = y
    elif i == 'D':
        if y != n:
            y += 1
        else:
            y = y
print(x,y)