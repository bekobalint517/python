egyik = int(input("Addjon meg egy számot"))
masik = int(input("Addjon meg egy másik számot"))
jel = input("Addjon megy egy műveleti jelet")

print('A művelet eredménye:', end ='')
if jel == '+':
    print(egyik+masik)
    
elif jel == '-':
    print(egyik-masik)

elif jel == '%':
    print(egyik % masik)

elif jel == '/':
    print(egyik / masik)

elif jel == '>>':
    print(egyik >> masik)    




