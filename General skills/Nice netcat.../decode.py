f = open('text.txt')
s = ''
for l in f:
    i = int(l)
    s += chr(i)
print(s)