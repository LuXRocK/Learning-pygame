from posixpath import split


f = open('przyklad.txt', 'r')

lines = []

for i in f:
    lines.append(i.split())
napis = []
for line in lines:
    if line // 39:
        napis.append(line)
# print(lines)
print(napis)
