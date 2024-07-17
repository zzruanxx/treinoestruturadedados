#treino de estrutura de dados , introdução a estruturas de dados - 3 Semestre

# exemplos de  manipulação de listas

lista = [1,2,3,4,5]

print(lista[3])

print(lista[2])

print(lista)

#adição de elementos

lista.append(6)

print(lista[5])

#remoção de elementos

lista.remove(2)

print(lista[2])

print(lista)

# iteração - for   in

for elemento in lista:
    print(2)

#tuplas - sequencias imutáveis, frequentemente usada para armazenar coleção de itens heterogeneos

tupla = (1, 'dois', 3.5)

print(tupla[1])

print (tupla [2])

print(tupla)

# desempacotamento de tupla

a,b,c = tupla
print(a,b,c)