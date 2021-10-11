lista1 = [3, 4, 1, 5, 1, 1]
lista2 = [2, 3, 4, 3, 2, 1]
lista3 = [0, 0, 0, 0, 0, 0]

for i in range(6):
    lista3[i] = lista1[i] + lista2[i]

print(lista3)