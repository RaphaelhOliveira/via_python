modelos = []
ultimo_id_modelo = 0

print("=== MODELO ===")

ultimo_id_modelo += 1
id_modelo = ultimo_id_modelo

nome_modelo = input("Nome do modelo: ")
ano_lancamento = input("Ano de lançamento: ")
categoria = input("Categoria: ")

modelos.append({
    'id': id_modelo,
    'nome_modelo': nome_modelo,
    'ano_lancamento': ano_lancamento,
    'categoria': categoria
})

print("\n=== DADOS MODELO ===")
print(f"ID: {id_modelo}")
print(f"Nome do modelo: {nome_modelo}")
print(f"Ano de lançamento: {ano_lancamento}")
print(f"Categoria: {categoria}")
