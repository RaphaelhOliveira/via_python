clientes = []
ultimo_id_cliente = 0

print("=== CADASTRO DE CLIENTE ===")

ultimo_id_cliente += 1
id_cliente = ultimo_id_cliente

nome = input("Nome: ")

while True:
    cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    if len(cpf) == 11 and cpf.isdigit():
        break
    else:
        print("❌ CPF deve ter exatamente 11 dígitos numéricos. Tente novamente.")

while True:
    telefone = input("Telefone: ").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) == 11 and telefone.isdigit():
        break
    else:
        print("❌ Telefone deve ter exatamente 11 dígitos numéricos. Tente novamente.")

email = input("Email: ")
endereco = input("Endereço: ")
data_cadastro = input("Data de cadastro (DD/MM/AAAA): ")

clientes.append({
    'id': id_cliente,
    'nome': nome,
    'cpf': cpf,
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
    'data_cadastro': data_cadastro
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_cliente}")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"Email: {email}")
print(f"Endereço: {endereco}")
print(f"Data de cadastro: {data_cadastro}")
