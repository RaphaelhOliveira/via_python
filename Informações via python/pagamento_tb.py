pagamentos = []
ultimo_id_pagamento = 0

print("=== PAGAMENTO ===")

ultimo_id_pagamento += 1
id_pagamento = ultimo_id_pagamento

valor_pago = input("Valor pago: R$ ")
data_pagamento = input("Data de pagamento (DD/MM/AAAA): ")
metodo = input("Método de pagamento: ")

pagamentos.append({
    'id': id_pagamento,
    'valor_pago': valor_pago,
    'data_pagamento': data_pagamento,
    'metodo': metodo
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_pagamento}")
print(f"Valor pago: R$ {valor_pago}")
print(f"Data de pagamento: {data_pagamento}")
print(f"Método: {metodo}")
