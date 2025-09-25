fornecedores = []
ultimo_id_fornecedor = 0

print("=== FORNECEDOR ===")

ultimo_id_fornecedor += 1
id_fornecedor = ultimo_id_fornecedor

nome = input("Nome do fornecedor: ")

while True:
    cnpj = input("CNPJ: ").replace(".", "").replace("/", "").replace("-", "").replace(" ", "")
    if len(cnpj) == 14 and cnpj.isdigit():
        break
    else:
        print("❌ CNPJ deve ter exatamente 14 dígitos numéricos. Tente novamente.")

while True:
    telefone = input("Telefone: ").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) == 11 and telefone.isdigit():
        break
    else:
        print("❌ Telefone deve ter exatamente 11 dígitos numéricos. Tente novamente.")

email = input("Email: ")
endereco = input("Endereço: ")

fornecedores.append({
    'id': id_fornecedor,
    'nome': nome,
    'cnpj': cnpj,
    'telefone': telefone,
    'email': email,
    'endereco': endereco
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_fornecedor}")
print(f"Nome: {nome}")
print(f"CNPJ: {cnpj}")
print(f"Telefone: {telefone}")
print(f"Email: {email}")
print(f"Endereço: {endereco}")
