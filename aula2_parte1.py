# --------------------------------------------------------
# Exemplo 1: Loop while
# --------------------------------------------------------
# A variável 'pessoas' inicia em 2 e, enquanto for menor ou igual a 32,
# o loop imprime uma mensagem e incrementa o valor em 1 a cada iteração.
pessoas = 2
while pessoas <= 32:
    print(f"A Instrutorissíma Fernanda deve {pessoas} pessoas")
    pessoas += 1

# Bloco para entrada de dados via input (comentado):
# resposta = input("Digite sua resposta [S/N]: ")
# while resposta.upper() == "S":
#     print("A sua resposta foi sim, irei executar novamente!!!")
#     resposta = input("Digite sua resposta [S/N]: ")

# --------------------------------------------------------
# Exemplo 2: Loop for para iterar sobre listas
# --------------------------------------------------------

# Lista com os nomes que Fernanda deve
fernanda_deve_pessoas = [
    "Amandah", "Tulani", "Renato", "Stephanny", "Nathalia", "Camila", "Hayde", "Maria Eduarda"
]
for item in fernanda_deve_pessoas:
    print(f"A Fernanda deve à(o) {item}")

# Lista de cores para exibir uma pergunta
cores = ["Vermelho", "Rosa", "Preto", "Branco", "Verde", "Tomato"]
for cor in cores:
    print(f"Qual sua cor favorita: {cor}?")

# --------------------------------------------------------
# Exemplo 3: Manipulação de Strings
# --------------------------------------------------------

# Exemplo 3.1: Transformações básicas em uma string
usuaria = "fernanda"
print(usuaria.capitalize())  # Converte a primeira letra para maiúscula: "Fernanda"
print(usuaria.upper())       # Converte todas as letras para maiúsculas: "FERNANDA"

# Exemplo 3.2: Combinação de métodos para manipulação de strings
nome_sobrenome_usuaria = "fernanda tomato"
# Capitaliza a string e substitui "tomato" por "Correa"
print(nome_sobrenome_usuaria.capitalize().replace("tomato", "Correa"))

# Exemplo 3.3: Dividindo uma string em uma lista com base em um delimitador
nome_sobrenome = "Fernanda-Correa"
# O método split utiliza o hífen como delimitador para separar a string em uma lista.
print(nome_sobrenome.split('-'))  # Resultado: ['Fernanda', 'Correa']

# Exemplo 3.4: Juntando elementos de uma lista em uma única string com join
lista_nomes = ["Fernanda", "João", "Amandah", "Felipe", "ciclano", "beltrano", "zumano", "romano", "fulano"]
# Os elementos da lista serão unidos em uma única string, separados por " - ".
print(" - ".join(lista_nomes))
