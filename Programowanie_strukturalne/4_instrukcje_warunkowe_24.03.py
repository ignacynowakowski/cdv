#instrukcje warunkowe

x = 5;
if x == 5:
    print("x jest równe 5")
    x= str(x)
    print("Wyświetlam wartość zmiennej x:" + x)
else:
    print("x jest różne od ")
    print("Wyświetlam wartość zmiennej x:" + x)

#######

y = True
if y:
    print("Prawda")
else:
    print("Fałsz")

########

z = 5 > 6
if z:
    print("Prawda")
else:
    print("Fałsz")
print(z)

########

j = "1"
if bool(j):
    print("Prawda " + j)
else:
    print("Fałsz " + j)
