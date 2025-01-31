# 📝 Variáveis em Diferentes Linguagens de Programação
# React -> Estados (useState)
# JavaScript -> var, let e const
# Python -> nome_da_variavel

# Exemplos de variáveis em Python:
nome = "Fulano da Silva"
idade = 16
cantora = "Fernanda Correa"

# 🏷️ Nomenclatura de Variáveis

# camelCase -> Padrão de nomenclatura onde a primeira palavra começa com letra minúscula,
# e as seguintes iniciam com letra maiúscula.
primeiroNomeSobrenome = "Danilo Almeida"

# snake_case -> Padrão de nomenclatura onde as palavras são separadas por underscores (_).
primeiro_nome_sobrenome = "Hugo França"

# 🔒 CONSTANTES -> Por convenção, variáveis que não devem ser alteradas são escritas em letras maiúsculas.
TIPO_CARRO = "UNO"

# 🛠️ Tipos de Dados em Python

# 🔢 Inteiros (int) -> Números positivos ou negativos sem casas decimais.
temperatura = -273
idade_da_terra = 45000000000000000000000000000000000000000000000000000000000000000000000000  # Exemplo exagerado de um número muito grande.

# 🧮 Ponto Flutuante (float) -> Números com casas decimais (usando ponto ao invés de vírgula).
pi = 3.14159
preco = 49.99

print(preco)  # Exibe o valor da variável 'preco'

# 🔠 Strings (str) -> Dados textuais, definidos entre aspas simples ('') ou duplas ("").
dados_textuais = "Arcane é a melhor série da história universal, mundial, global, interdimensional, espacial e multiversal."

print(dados_textuais)

frase_pontuada = "Agora são 6 e ônibus."

print(frase_pontuada)

# Podemos concatenar (juntar) strings de duas formas:
print(dados_textuais, frase_pontuada)  # Separa por espaço automaticamente
print(dados_textuais + frase_pontuada)  # Junta sem espaço extra

# ✅ Booleanos (bool) -> Representam valores Verdadeiro (True) ou Falso (False).
maior_de_dezoito = True
print(maior_de_dezoito)

aula_amanha = False
print(aula_amanha)

# 🚫 Nulos (None) -> Representam a ausência de valor (ou valor indefinido).
vazio = None
print(vazio)

# 🔍 type() -> Função que retorna o tipo de dado de uma variável.
print(type(aula_amanha))  # Exibe "<class 'bool'>"

# 🎨 f-strings (formatted strings) -> Forma prática de inserir variáveis dentro de strings.
tema_aula = "Python, Passarela, Rato, Arcane"

print(f"O tema da aula de hoje é {tema_aula}.")
