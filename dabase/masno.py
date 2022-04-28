f = open('szuster.txt', 'r')
lines = [line.split() for line in f]
xandy = []
i1i2 = []
for line in lines:
    xy = [line[0],line[1]]
    i_s = [line[2], line[3]]
    xandy.append(xy)
    i1i2.append(i_s)
odwiedzone = []
curr_i = 0
next_step = 1
while True:
    # i = int(i1i2[next_step][curr_i])
    if next_step==0:
        print('ruchanie')
        break
    next_step = int(i1i2[next_step-1][curr_i])
    odwiedzone.append(next_step)
    if next_step in odwiedzone:
        if curr_i == 1:
            print('oba nieskończone')
            break
        odwiedzone = []
        curr_i = 1 
        next_step = 1
        print('nieskonczoan petla 1')
else:
    exit()
print(odwiedzone)

for x in odwiedzone:
    print(xandy[x-1][0],' ',xandy[x-1][1],' ',end='')
# print(xandy)
# print(i1i2)
# print(lines)