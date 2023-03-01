# string de entrada
string = 'exemplo'

# conversão da string para uma lista de caracteres
lista_caracteres = list(string)

# inversão dos caracteres
for i in range(len(lista_caracteres) // 2):
    j = len(lista_caracteres) - i - 1
    lista_caracteres[i], lista_caracteres[j] = lista_caracteres[j], lista_caracteres[i]

# conversão da lista de caracteres de volta para uma string
string_invertida = ''.join(lista_caracteres)

# impressão do resultado
print(string_invertida)
