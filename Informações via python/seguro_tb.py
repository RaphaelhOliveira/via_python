seguros = []
ultimo_id_seguro = 0

print("=== SEGURO ===")

ultimo_id_seguro += 1
id_seguro = ultimo_id_seguro

empresa_seguro = input("Empresa do seguro: ")
valor_premio = input("Valor do prêmio: R$ ")
cobertura = input("Cobertura: ")
validade = input("Validade (DD/MM/AAAA): ")

seguros.append({
    'id': id_seguro,
    'empresa_seguro': empresa_seguro,
    'valor_premio': valor_premio,
    'cobertura': cobertura,
    'validade': validade
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_seguro}")
print(f"Empresa do seguro: {empresa_seguro}")
print(f"Valor do prêmio: R$ {valor_premio}")
print(f"Cobertura: {cobertura}")
print(f"Validade: {validade}")
