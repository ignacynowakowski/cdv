programowanie = ["python", "c#", "js", "PHP", "java"]

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print("Pierwszy język programowania: " + pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatni = programowanie[-1]
print(ostatni)

#Dodawanie nowego elementu na końcu listy
programowanie.append("R")
print(programowanie)

pr

#Zliczanie elementów w liście
programowanie.append("python")
ile = programowanie.count("python")
print(ile)

iloscElementow = len(programowanie)
#print("Ilosć elementów e liście", ilośćElementow)
print("Ilosć elementów e liście", end="")
print(iloscElementow)

#Połączenie list
