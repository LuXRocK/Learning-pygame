


iksy = [1, 4, 1, 1, 1, 1, 1, 2, 4]
igreki = [13, 2, 10, 3, 5, 9, 2, 4, 6]
wyniki = []
k = 0
i = 1
while i <= len(iksy):
    if iksy[i]/igreki[i] < iksy[k]/igreki[k]:
        k = i
    x, y = iksy[k], igreki[k]
    i += 1
    wyniki.append((x,y))
    # iksy.pop(k)
    # igreki.pop(k)
    
print(x, y)
print(wyniki)