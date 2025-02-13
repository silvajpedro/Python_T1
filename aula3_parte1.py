# 📌 Tuplas -> São estruturas que armazenam múltiplas informações, porém **são imutáveis**,
# ou seja, não podem ser alteradas após a criação.

# Exemplo de tupla com devedores
devedores = ("Waldecy", "Vagner", "Jakeline", "Luciana", "Emanuelle", "Gabrielle")
#               0          1          2           3            4           5

# Exibindo um elemento da tupla pelo índice
print(f"⚠️ Primeiro devedor: {devedores[0]}")

# 🚨 O código abaixo gera erro, pois tuplas são imutáveis!
# devedores[1] = "Ezequiel"  # ❌ Isso não é permitido!

# Criando uma tupla vazia
pessoas = ()

# Exibindo o tipo da variável
print("\n📌 Tipo da variável 'pessoas':", type(pessoas))  # Saída: <class 'tuple'>

# Tupla vazia será convertida para lista para permitir modificações
pessoas = list(pessoas)

# Exibindo o novo tipo após a conversão
print("📌 Tipo após conversão para lista:", type(pessoas))  # Saída: <class 'list'>

# Adicionando informações à lista
pessoas.append("Douglas")
pessoas.append(1234567890)
pessoas.append(9876543212)

# Convertendo de volta para tupla
pessoas = tuple(pessoas)

# Exibindo a tupla final
print("\n✅ Tupla modificada:", pessoas)
print("📌 Tipo final:", type(pessoas))  # Saída: <class 'tuple'>

# Criando um cadastro de cliente utilizando tupla
cliente = ()
cliente = list(cliente)  # Convertendo para lista para adicionar dados
cliente.append("Lívia")
cliente.append(9876543210)
cliente.append("10/02/2025")
cliente = tuple(cliente)  # Convertendo de volta para tupla

print("\n👤 Dados do cliente cadastrados:", cliente)

# Criando uma tupla a partir de uma lista existente
usuario = ["Luis", 2345678912, "11/02/2025"]
usuario = tuple(usuario)

print("\n👤 Usuário cadastrado:", usuario)

# Criando uma tupla vazia e adicionando um valor
data = ()
data = list(data)  # Convertendo para lista
data.append("qualquer coisa joão")
data = tuple(data)  # Convertendo de volta para tupla

print("\n📌 Dados armazenados na tupla:", data)

# 📌 Funções -> São blocos de código que executam tarefas específicas e podem ser reutilizados.

# 🔹 Exemplo de operações matemáticas sem função
print("\n📌 Operações matemáticas simples:")
print(21324 + 3435436653)
print(34456 - 123)

# 🔹 Exemplo de função simples de soma
def soma():
    """Função que imprime a soma de 1 + 1."""
    print(1 + 1)

# Chamando a função várias vezes
print("\n📌 Chamando a função de soma:")
soma()
soma()
soma()
