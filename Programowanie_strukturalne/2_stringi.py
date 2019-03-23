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

text1 = 'Jan\n'
text2 = 'Nowak'
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + ' ' + text2)

#wyświetlanie łańcuchów znaków

#wszystkie wersje pythona
text = '%a, Java i %a' % ('PHP', "Pythine")
print(text)

#nowsze wersje pythona 2.6 i > 3
text = '{0}, Java i {1}'.format("PHP", "Python")

#help(text.teplace)

new = text.replace('PHP', "C#")
print(new)

#wypisywanie danych
rok = "2019"
misiac = 'marzec'
dzien = '23'

# print('Data: ' + end="")
print(dzien, miesiac, rok)

# print('Data: ' + end="")