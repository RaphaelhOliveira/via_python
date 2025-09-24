fabricantes = []
ultimo_id_fabricante = 0

print("=== FABRICANTE ===")

ultimo_id_fabricante += 1
id_fabricante = ultimo_id_fabricante

nome = input("Nome do fabricante: ")
pais_origem = input("País de origem: ")

while True:
    telefone_contato = input("Telefone de contato: ").replace("(", "").replace(")", "").replace("-", "").replace(" ", "").replace("+", "")
    if len(telefone_contato) == 11 and telefone_contato.isdigit():
        break
    else:
        print("❌ Telefone deve ter exatamente 11 dígitos numéricos. Tente novamente.")

fabricantes.append({
    'id': id_fabricante,
    'nome': nome,
    'pais_origem': pais_origem,
    'telefone_contato': telefone_contato
})

print("\n=== DADOS FABRICANTE ===")
print(f"ID: {id_fabricante}")
print(f"Nome: {nome}")
print(f"País de origem: {pais_origem}")
print(f"Telefone de contato: {telefone_contato}")
