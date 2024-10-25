# # Cadastro do usuário
# usuarios = []
# nome = input("Digite seu nome: ")
# email = input("Digite seu email: ")
# usuarios.append({'nome': nome, 'email': email})

# # Produtos disponíveis
# produtos = ["Camiseta - R$ 50,00", "Calça - R$ 80,00", "Tênis - R$ 120,00"]
# precos = [50.0, 80.0, 120.0]
# escolhas_produto = []

# # Exibição dos produtos
# print("Produtos disponíveis:")
# for i in range(3):
#     print(f"{i + 1}. {produtos[i]}")

# # Compra de um produto
# produto_escolhido = int(input("Escolha o número do produto que deseja comprar (1-3): ")) - 1
# quantidade = int(input("Quantas unidades deseja comprar? "))
# escolhas_produto.append(produto_escolhido)

# # Cálculo do valor total
# valor_total = precos[produto_escolhido] * quantidade

# # Exibição do valor total
# print(f"Valor total da compra: R$ {valor_total:.2f}")

# # Pagamento
# forma_pagamento = input("Escolha a forma de pagamento (Cartão, Dinheiro): ")
# if forma_pagamento.lower() == "cartão":
#     print("Pagamento realizado com cartão.")
# elif forma_pagamento.lower() == "dinheiro":
#     print("Pagamento realizado em dinheiro.")
# else:
#     print("Forma de pagamento inválida.")

# # Resumo da compra
# print(f"Cliente: {usuarios[0]['nome']}, Produto: {produtos[produto_escolhido]}, Quantidade: {quantidade}, Valor Total: R$ {valor_total:.2f}")











# Cadastro de Clientes
clientes = []
idades = []

# Cadastro dos clientes
for i in range(3):
    nome = input(f"Digite o nome do cliente {i+1}: ")
    idade = int(input(f"Digite a idade do cliente {i+1}: "))
    clientes.append(nome)
    idades.append(idade)

# Reservas de Quartos
tipos_quarto = ["Simples", "Duplo", "Luxo"]
precos_quarto = [100.0, 150.0, 250.0]
escolhas_quarto = []

for i in range(3):
    escolha = input(f"Cliente {clientes[i]}, escolha o tipo de quarto (Simples, Duplo, Luxo): ")
    escolhas_quarto.append(escolha)

# Cálculo da Estadia
dias = []
valores_totais = []

for i in range(3):
    dias_cliente = int(input(f"Quantos dias o cliente {clientes[i]} ficará no hotel? "))
    dias.append(dias_cliente)

    if escolhas_quarto[i] == "Simples":
        valor_cliente = precos_quarto[0] * dias_cliente
    elif escolhas_quarto[i] == "Duplo":
        valor_cliente = precos_quarto[1] * dias_cliente
    elif escolhas_quarto[i] == "Luxo":
        valor_cliente = precos_quarto[2] * dias_cliente
    else:
        valor_cliente = 0  # caso não seja uma escolha válida
    
    valores_totais.append(valor_cliente)

# Pagamento
desconto = 0.1  # 10% de desconto
valores_a_pagar = []

for i in range(3):
    valor_final = valores_totais[i] * (1 - desconto) if idades[i] < 18 else valores_totais[i]
    valores_a_pagar.append(valor_final)

# Exibição dos Resultados
for i in range(3):
    print(f"Cliente: {clientes[i]}, Tipo de Quarto: {escolhas_quarto[i]}, Dias: {dias[i]}, Valor Total: R$ {valores_totais[i]:.2f}, Valor a Pagar: R$ {valores_a_pagar[i]:.2f}")