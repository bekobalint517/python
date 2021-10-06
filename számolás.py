#2-100 prímszámok
"""
for x in range(101,1,-2):
    print(x)
"""
for szám in range(2,101):
    for osztó in range:(2,x//2+1)#4 nem lesz prím
        #print(x, osztó)
        if (szám % osztó) == 0:
            break
    else:
        print(x, 'prím')