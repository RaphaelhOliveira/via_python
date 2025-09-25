promocoes = []
ultimo_id_promocao = 0

print("=== PROMOÇÃO ===")

ultimo_id_promocao += 1
id_promocao = ultimo_id_promocao

descricao = input("Descrição da promoção: ")
desconto_percentual = input("Desconto percentual (%): ")
data_inicio = input("Data de início (DD/MM/AAAA): ")
data_final = input("Data final (DD/MM/AAAA): ")

promocoes.append({
    'id': id_promocao,
    'descricao': descricao,
    'desconto_percentual': desconto_percentual,
    'data_inicio': data_inicio,
    'data_final': data_final
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_promocao}")
print(f"Descrição: {descricao}")
print(f"Desconto percentual: {desconto_percentual}%")
print(f"Data de início: {data_inicio}")
print(f"Data final: {data_final}")
