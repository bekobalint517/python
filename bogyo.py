nev = input('Mi a neve?')
print(nev)
bogyo = int(input('Hány darabot gyüjtöttél?'))
if bogyo < 10:
    minősítés = 'zsenge'
elif bogyo > 10:
    minősítés = 'profi'
print(f'{nev}, minősítése {minősítés}')