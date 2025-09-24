manutencoes = []
ultimo_id_manutencao = 0

print("=== MANUTENÇÃO DE CARRO ===")

ultimo_id_manutencao += 1
id_manutencao = ultimo_id_manutencao

descricao = input("Descrição da manutenção: ")
data_manutencao = input("Data de manutenção (DD/MM/AAAA): ")
custo = input("Custo: R$ ")

manutencoes.append({
    'id': id_manutencao,
    'descricao': descricao,
    'data_manutencao': data_manutencao,
    'custo': custo
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_manutencao}")
print(f"Descrição: {descricao}")
print(f"Data de manutenção: {data_manutencao}")
print(f"Custo: R$ {custo}")
