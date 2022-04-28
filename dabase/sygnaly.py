from posixpath import split


f = open('przyklad.txt', 'r')
lines = f.readlines(split())

print(lines)
