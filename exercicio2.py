# Crie um sistema de consulta de preços
 
# Seu sistema deve:
 
# Pedir para o usuário o nome de um produto

# Caso o produto exista na lista de produtos, o programa deve

# retornar o preço do produto como resposta
 
# Ex: O produto celular custa R$1500

# Caso o produto não exista na lista de produtos, o programa deve

# printar uma mensagem para o usuário tentar novamente
 
# Celular: 1500, câmera: 1000, fone de ouvido: 800, monitor: 2000
# Caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto.
 
# Se ele responder sim, o programa deve pedir o nome do produto e o preço do produto e cadastrar no dicionário de preços.
 
# Em seguida do cadastro bem sucedido, o programa deve imprimir o
# dicionário de preços atualizado.

# Dicionário 
precos = {
    'celular': 1500,
    'câmera': 1000,
    'fone de ouvido': 800,
    'monitor': 2000
}


produtos = input("Digite o nome do produto para consultar: ").lower()

if produtos in precos:
    print(f"O produto {produtos} custa R${precos[produtos]}")
else:
    print("Produto não encontrado. tente novamente ou cadastre um novo produto")
    resposta = input("Digite 'tentar' para tentar novamente ou 'cadastrar' para cadastrar um novo produto: ").lower()
    
    if resposta == 'cadastrar':
        nomeproduto = input("Digite o nome do novo produto: ").lower()
        precoproduto = float(input("Digite o preço do novo produto: "))
        precos[nomeproduto] = precoproduto
        print("Produto cadastrado com sucesso!")
        print("Lista atualizada de produtos e preços:")
        for produto, preco in precos.items():
            print(f"{produto}: R${preco}")
    else:
        print("Resposta inválida. Encerrando.")