transacoes = []
ultimo_id_transacao = 0

print("=== TRANSAÇÃO ===")


ultimo_id_transacao += 1
id_transacao = ultimo_id_transacao

data_transacao = input("Data da transação (DD/MM/AAAA): ")
valor_total = input("Valor total: R$ ")
forma_pagamento = input("Forma de pagamento: ")

transacoes.append({
    'id': id_transacao,
    'data_transacao': data_transacao,
    'valor_total': valor_total,
    'forma_pagamento': forma_pagamento
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_transacao}")
print(f"Data da transação: {data_transacao}")
print(f"Valor total: R$ {valor_total}")
print(f"Forma de pagamento: {forma_pagamento}")
