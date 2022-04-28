a = 282
b = 78
def nwd(a,b):
    # while True:
    #     b = a%b
    #     a = b
    #     if b == 0:
    #         break
    # return a
    reszta = a%b 
    while reszta != 0:
        a = b 
        b = reszta 
        reszta = a%b
    return b
print(nwd(a,b))



        
