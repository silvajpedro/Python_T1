# ----------------------------------------
# Exibindo mensagem de boas-vindas
# ----------------------------------------

print("Restaurante Vai com Tudo!")  # Mensagem inicial do restaurante

# ----------------------------------------
# Solicitando informações sobre o pedido
# ----------------------------------------

pedido_cliente = input("Olá, querido cliente! Qual seu prato? ")  # Captura o prato escolhido
bebida_cliente = input("E o que gostaria de beber? ")  # Captura a bebida escolhida

# Exibindo o pedido formatado
print(f'O seu pedido foi registrado: {pedido_cliente} acompanhado de {bebida_cliente}.')

# ----------------------------------------
# Entrada e saída de dados com conversão de tipos
# ----------------------------------------

# Solicita os preços do prato e da bebida e os converte para float
valor_prato = float(input(f'O valor do seu pedido {pedido_cliente} é de: R$ '))
valor_bebida = float(input(f'O valor da sua bebida {bebida_cliente} é de: R$ '))

# Calculando o total do pedido
total = valor_prato + valor_bebida

# Exibindo o total sem formatação decimal fixa
print(f'O valor total ficou em: R$ {total}')

# ----------------------------------------
# Estruturas Condicionais para controle de fluxo
# ----------------------------------------

saldo = True  # Variável indicando se há saldo disponível
idade = 16  # Definição de uma idade fictícia

# Condicional Simples
# Se o saldo for False (não há dinheiro), exibe uma mensagem
if not saldo:
    print("Tá lascado!")
    print("Sinto muito pela sua situação, também tô assim!!!")

# Condicional Composta
# Se tem saldo, pode mandar um pix, senão, está "lascado"
if saldo:
    print("Você pode mandar um pix aos seus instrutores!!! ;D")
else:
    print("Tá lascado!")

# Condicional Aninhada
# Verifica múltiplas condições de saldo e idade
if not saldo and idade >= 18:
    print("Sinto muito, não pode mandar um pix aos seus instrutores!")
elif saldo and idade >= 18:
    print("Uhuuuuuul, TA TA TA TA, você pode mandar um pix para os seus instrutores!!!")
else:
    print("Não precisa de pix, a sua presença em sala de aula já é maravilhosa! <3")

# ----------------------------------------
# Verificando o prato e a bebida do dia
# ----------------------------------------

prato_do_dia = "Salada"  # Definição do prato do dia
bebida_do_dia = "Suco Verde"  # Definição da bebida do dia

# Estrutura condicional para verificar o prato e a bebida do dia
if prato_do_dia == "Churrasco com Fritas" and bebida_do_dia == "Coca gelada":
    print("Uhuuuuul, convide os seus instrutores para estarem com você!!!")
elif prato_do_dia == "Estrogonofe de Carne" and bebida_do_dia == "Coca gelada":
    print("Ta Ta ta ta, convide os seus instrutores também, eles gostam!")
else:
    print("Eita, deixa pra próxima!!!")

# ----------------------------------------
# Operadores de Comparação e Lógicos
# ----------------------------------------

# Operadores de Comparação:
# >  : Maior que
# <  : Menor que
# >= : Maior ou igual a
# <= : Menor ou igual a
# != : Diferente de
# == : Igual a

# Exemplo prático
a = 20
b = 10

print(f'{a} > {b}:', a > b)   # True  -> Verifica se "a" é maior que "b"
print(f'{a} < {b}:', a < b)   # False -> Verifica se "a" é menor que "b"
print(f'{a} >= {b}:', a >= b) # True  -> Verifica se "a" é maior ou igual a "b"
print(f'{a} <= {b}:', a <= b) # False -> Verifica se "a" é menor ou igual a "b"
print(f'{a} == {b}:', a == b) # False -> Verifica se "a" é igual a "b"
print(f'{a} != {b}:', a != b) # True  -> Verifica se "a" é diferente de "b"

# Operadores Lógicos:
# - and (E): Retorna True se ambas as condições forem verdadeiras
# - or (OU): Retorna True se pelo menos uma das condições for verdadeira
# - not (Negação): Inverte o valor booleano da condição

# ----------------------------------------
# Exemplo prático de verificação de idade e saldo
# ----------------------------------------

if idade > 18 and saldo:
    print("Pode pedir qualquer item do cardápio! 🍔🥤")
elif idade > 18 and not saldo:
    print("Infelizmente, você precisa de saldo para comprar. 😔")
else:
    print("Ainda não pode comprar sem um responsável. 👨‍👩‍👦")
