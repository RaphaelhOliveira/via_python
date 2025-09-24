financiamentos = []
ultimo_id_financiamento = 0

print("=== FINANCIAMENTO ===")

ultimo_id_financiamento += 1
id_financiamento = ultimo_id_financiamento

banco_parceiro = input("Banco parceiro: ")
valor_financiado = input("Valor financiado: R$ ")
quantidade_parcelas = input("Quantidade de parcelas: ")
taxa_juros = input("Taxa de juros (%): ")

financiamentos.append({
    'id': id_financiamento,
    'banco_parceiro': banco_parceiro,
    'valor_financiado': valor_financiado,
    'quantidade_parcelas': quantidade_parcelas,
    'taxa_juros': taxa_juros
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_financiamento}")
print(f"Banco parceiro: {banco_parceiro}")
print(f"Valor financiado: R$ {valor_financiado}")
print(f"Quantidade de parcelas: {quantidade_parcelas}")
print(f"Taxa de juros: {taxa_juros}%")
