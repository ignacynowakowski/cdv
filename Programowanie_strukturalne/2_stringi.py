tekst = 'Anna, paweł, TOmEk'
tab = tekst.split(', ')

print(tekst)
print(tab)

imie1 = tab[0]
print(imie1)

print("twoje imię: "+imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzanie zawartosci
zawartosc = imie1.isalpha();
print(zawartosc)
print(type(zawartosc))

imie = 'Julia'
print('\nDane użytkownika\nMasz na imię: '+imie)