# Listas -> Arrays, Vetores, Matrizes --> São variáveis que conseguem guardar uma quantidade muito grande de informações, porém não de forma organizada.

# Criando uma lista com diferentes tipos de dados
lista_dos_sonhos = ["pizza de 8 sabores", "Morar na Suíça", "Pastel de 32 Sabores", "Pizza de Tanajura", 12, 3.78, True, False, "Douglas elogiando o Python!!!", "Cris aprendendo Python!!!"]

# Exibindo a lista completa
print(lista_dos_sonhos)

# Acessando elementos individuais da lista pelo índice
print(lista_dos_sonhos[1])  # Segundo elemento
print(lista_dos_sonhos[2])  # Terceiro elemento
print(lista_dos_sonhos[3])  # Quarto elemento

# Ordenando a lista em ordem alfanumérica (irá gerar erro se houver tipos mistos)
# lista_dos_sonhos.sort()  # Isso funcionaria apenas se todos os itens fossem do mesmo tipo
# print(lista_dos_sonhos)

# Indexação Negativa -> Permite acessar elementos da lista de trás para frente
print(lista_dos_sonhos[-1])  # Último elemento da lista
print(lista_dos_sonhos[-2])  # Penúltimo elemento

# Verificando o tipo de dado da lista e seu tamanho
print(type(lista_dos_sonhos))  # Mostra que o tipo é 'list'
print(len(lista_dos_sonhos))  # Retorna a quantidade de elementos na lista

# Manipulação de listas - Métodos comuns

# insert -> Adiciona um elemento em uma posição específica da lista
lista_dos_sonhos.insert(0, "Thamyres vai patrocinar nossa aposentadoria!!!")
lista_dos_sonhos.insert(3, "Tomar café")
print(lista_dos_sonhos)

# append -> Adiciona um elemento ao final da lista
lista_dos_sonhos.append("Ser poliglota")
print(lista_dos_sonhos)

# sort -> Ordena a lista em ordem alfabética (crescente ou decrescente)
nomes = ["Joaquim", "Fernanda", "Douglas", "Vinicius", "Leonardo", "Argel", "Enzo", "Marlon", "Grazi", "Emanuelle", "Natália", "Bernardo"]
nomes.sort()  # Ordenação crescente (A-Z)
print(nomes)
nomes.sort(reverse=True)  # Ordenação decrescente (Z-A)
print(nomes)

# Trabalhando com listas numéricas
numeros = [1000, 345, 126, 579, 2, 20, 34, 67, 1]
numeros.sort()  # Ordenação crescente
print(numeros)

# remove -> Remove um elemento específico pelo valor fornecido
numeros.remove(1)  # Remove o número 1 da lista
print(numeros)

# pop -> Remove um elemento pelo índice informado
numeros.pop(0)  # Remove o primeiro elemento da lista
print(numeros)

# Cadastro de pessoas usando listas
cadastro = []
qntd_pessoas = int(input("Quantas pessoas deseja cadastrar? "))

# Loop para adicionar os nomes na lista de cadastro
while len(cadastro) < qntd_pessoas:
    cadastro.append(input("Digite o nome a ser adicionado: "))

# Exibindo os nomes cadastrados
print(f'As pessoas cadastradas foram: {cadastro}')
