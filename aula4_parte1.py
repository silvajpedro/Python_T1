# ----------- Funções em Python -----------
# Funções são responsáveis por executar ações de forma programática,
# sendo ativadas em momentos de interação do usuário.

print("Bom diaaa, usuário! Seja bem-vindo ao Vai No Coffe!!!")

# Solicitando credenciais do usuário
login = input("Digite seu e-mail: ")
senha = int(input("Digite sua senha: "))  # Senha como número inteiro

def boas_vindas():
    """Exibe mensagem de boas-vindas ao usuário logado."""
    print(f"Bom diaaa, {login}! Seja bem-vindo ao Vai No Coffe!!!")

def login_invalido():
    """Exibe mensagem para login inválido."""
    print("Tente novamente, suas credenciais são inválidas!!!")

# Verificação de login
if login == "joaopedefeijao@gmail.com" and senha == 123:
    boas_vindas()
else:
    login_invalido()

# ----------- Dicionários em Python -----------

# Dicionários armazenam dados de forma organizada em pares chave:valor.
# Permitem guardar grande quantidade de informações acessíveis por chave.

nomes_clientes = {
    'cliente_mg': 'Douglas',
    'clientes_rj': ["Yuri", "Jakeline", "Leonardo", "Bernardo"],  # Lista dentro do dicionário
    'cliente_rs': 'Argel',
    'cliente_pe': 'Hugo',
    'cliente_pi': 'Davi',
    'cliente_sp': 'Vinicius',
    'cliente_pa': 'Marlon',
    'cliente_ce': 'Waldecy'
}

# Adicionando um novo cliente do Distrito Federal
nomes_clientes.update({"cliente_df": 'Leonardo'}) 

# Alterando o cliente de São Paulo
nomes_clientes["cliente_sp"] = "Danilo"

# Exibindo dicionário atualizado
print("\nLista de clientes atualizada:")
print(nomes_clientes)

# AS CHAVES DEVEM SER ÚNICAS, NÃO PODEM TER CHAVES REPETIDAS.

# () -> Tuplas: Utilizadas quando precisamos armazenar valores imutáveis (que não podem ser alterados).
# [] -> Listas: Utilizadas para armazenar grande quantidade de informações modificáveis, mas sem estrutura organizada.
# {} -> Dicionários: Armazenam grande quantidade de informações organizadas em pares chave:valor.

# Removendo um cliente de Minas Gerais
del nomes_clientes['cliente_mg']

# Exibindo dicionário após a remoção
print("\nLista de clientes após remoção:")
print(nomes_clientes)

# Adicionando um novo cliente ao grupo de clientes do Rio de Janeiro
nomes_clientes['clientes_rj'].append("Fernanda")

# Exibindo dicionário atualizado
print("\nLista de clientes após nova adição:")
print(nomes_clientes)

# ----------- Iteração no Dicionário -----------

# Iterando sobre as chaves do dicionário para exibir os estados dos clientes
print("\nOs estados dos clientes são:")
for estado in nomes_clientes:
    print(f"- {estado}")
