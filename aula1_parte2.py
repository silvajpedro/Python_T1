# Exibindo mensagem de boas-vindas
print("Bem-vindo à Lanchonete Vai No Lanche!")

# Solicitando informações sobre o pedido
salgado = input("Informe o seu salgado: ")
bebida = input("O que irá beber: ")

# Exibindo o pedido
print(f'O seu pedido foi {salgado} acompanhado de uma {bebida}.')

# Entrada e saída de dados com conversão de tipos
valor_salgado = float(input(f'Informe o valor do {salgado}: R$ '))
valor_bebida = float(input("Informe o valor da bebida: R$ "))

# Calculando e exibindo o total do pedido
total = valor_salgado + valor_bebida
print(f'O total a pagar é R$ {total},00')

# Estruturas condicionais para controle de fluxo
saldo = True  # Variável indicando se há saldo disponível

# Condicional simples
if not saldo:
    print("Tá lascado!")

# Condicional composta
idade = 26  # Definindo idade fictícia

if idade >= 18:
    print("Se quiser, pode mandar um pix para os seus instrutores!")
else:
    print("Você ainda não pode mandar um pix para os seus instrutores.")

# Condicional aninhada
if idade >= 18 and saldo:
    print("Você pode mandar um pix aos seus instrutores ;D")
elif idade >= 18 and not saldo:
    print("Você não pode mandar um pix aos seus instrutores ;(")
else:
    print("A sua presença em sala de aula é o melhor presente <3")

# Operadores Lógicos e de Comparação
# JavaScript --> && (and), || (or), ! (not)
# Python     --> and, or, not

# Operadores lógicos:
# - and (e): Retorna True se ambas as condições forem verdadeiras.
#   Exemplo: Eu quero sorvete e batata frita → True/False
#
# - or (ou): Retorna True se pelo menos uma das condições for verdadeira.
#   Exemplo: Eu quero sorvete ou batata frita → True/False
#
# - not (negação): Inverte o valor booleano da condição.
#   Exemplo: not True → False / not False → True

# Operadores de comparação:
# >  : Maior que
# <  : Menor que
# >= : Maior ou igual a
# <= : Menor ou igual a
# != : Diferente de
# == : Igual a
