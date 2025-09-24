funcionarios = []
ultimo_id_funcionario = 0

print("=== FUNCIONÁRIO ===")

ultimo_id_funcionario += 1
id_funcionario = ultimo_id_funcionario

nome = input("Nome: ")

while True:
    cpf = input("CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    if len(cpf) == 11 and cpf.isdigit():
        break
    else:
        print("❌ CPF deve ter exatamente 11 dígitos numéricos. Tente novamente.")

cargo = input("Cargo: ")

while True:
    telefone = input("Telefone: ").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) == 11 and telefone.isdigit():
        break
    else:
        print("❌ Telefone deve ter exatamente 11 dígitos numéricos. Tente novamente.")

email = input("Email: ")
salario = input("Salário: R$ ")
data_admissao = input("Data de admissão (DD/MM/AAAA): ")

funcionarios.append({
    'id': id_funcionario,
    'nome': nome,
    'cpf': cpf,
    'cargo': cargo,
    'telefone': telefone,
    'email': email,
    'salario': salario,
    'data_admissao': data_admissao
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_funcionario}")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Cargo: {cargo}")
print(f"Telefone: {telefone}")
print(f"Email: {email}")
print(f"Salário: R$ {salario}")
print(f"Data de admissão: {data_admissao}")
