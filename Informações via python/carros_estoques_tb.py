carros_estoque = []
ultimo_id_carro = 0

print("=== CARRO EM ESTOQUE ===")

ultimo_id_carro += 1
id_carro = ultimo_id_carro

cor = input("Cor: ")
chassi = input("Chassi: ")
ano_fabricacao = input("Ano de fabricação: ")
preco_compra = input("Preço de compra: R$ ")
preco_venda = input("Preço de venda: R$ ")
status = input("Status: ")

carros_estoque.append({
    'id': id_carro,
    'cor': cor,
    'chassi': chassi,
    'ano_fabricacao': ano_fabricacao,
    'preco_compra': preco_compra,
    'preco_venda': preco_venda,
    'status': status
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_carro}")
print(f"Cor: {cor}")
print(f"Chassi: {chassi}")
print(f"Ano de fabricação: {ano_fabricacao}")
print(f"Preço de compra: R$ {preco_compra}")
print(f"Preço de venda: R$ {preco_venda}")
print(f"Status: {status}")
