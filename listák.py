
zs = ["hello", 2.0, 5, [10, 20]]
print(zs)

szotar = ["alma", "sajt", "kutya"]
szamok = [17, 123]
ures_lista = []
print(szotar[0], szamok, ures_lista)

print(szamok)
for i in enumerate (szamok):
    print(i)

for (i , ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])


szamok = []
szamok.append(6)
szamok.append(20)
szamok.append(16)
szamok.append(4)
print(szamok)

szamok.insert(0,16)
print(szamok)
print(szamok.count(16))

szamok.extend([5, 9, 5, 11])
print(szamok)

print(szamok.index(9))

szamok.sort()
print(szamok)

szamok.remove(16)
print(szamok)

#Rendezzünk egy szöveges adatokat tartalmazó listát!
szoveg_lista = ["barack", "alma", "mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort()
print(szoveg_lista2)

import locale
import functools

locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")  # a nyelv és a kódolás beállítása
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort(key = functools.cmp_to_key(locale.strcoll))
print(szoveg_lista2)


#Ha a lista elemeit felsorolással adjuk meg, az utolsó után is tehetünk vesszőt:
lista= ['Semé', 'Noéé', 'Lámekhé', 'Mathuséláé', 'Énókhé', 'Járedé', 'Mahalaléelé', 'Kajnáné', 'Énósé', 'Sethé', 'Ádámé', ]
print (lista)

#stringekhez hasonlóan indexelhetők, illetve szeletelhetők:
lista[0] # első elem
print(lista[0])
lista[-1] # utolsó elem
print(lista[-1])
lista[0:-1]
print(lista[0:-1]) # 0. elemtől az utolós előttiig!

#! Figyelem
#Stringek esetében az indexelés és a szeletelés adott esetben azonos eredményt ad:
str = 'Károly'
print(str[0])
print(str[0:1])

#Listák esetében az analóg eljárás különböző eredményt ad:
print(lista[0])
print(lista[0:2])

#LÉPÉSKÖZ
#A stringeknél látott módon megadhatjuk, hogy a kezdőértéktől minden k-adik kerüljön csak az eredménybe:
print(lista[::4])  #['Semé', 'Énókhé', 'Énósé']
print(lista[1::4]) #['Noéé', 'Járedé', 'Sethé']
print(lista[2::4]) #['Lámekhé', 'Mahalaléelé', 'Ádámé']


#LISTÁK KÖZÖTTI ÉRTÉKADÁS
#Nehezen emészthető, de jobb az elején tisztázni: a python megkülönböztet sekély és mély másolatot:
shallow_copy= lista[:]
deep_copy=    lista
lista[0]= 'Sémé'
print(shallow_copy)
print(deep_copy)