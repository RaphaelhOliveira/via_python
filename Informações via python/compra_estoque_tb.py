compras_estoque = []
ultimo_id_compra = 0

print("=== COMPRA DE ESTOQUE ===")

ultimo_id_compra += 1
id_compra = ultimo_id_compra

data_compra = input("Data da compra (DD/MM/AAAA): ")
valor_compra = input("Valor da compra: R$ ")

compras_estoque.append({
    'id': id_compra,
    'data_compra': data_compra,
    'valor_compra': valor_compra
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_compra}")
print(f"Data da compra: {data_compra}")
print(f"Valor da compra: R$ {valor_compra}")
