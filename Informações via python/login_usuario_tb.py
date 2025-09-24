import hashlib

usuarios = []
ultimo_id = 0

print("=== CADASTRO DE USUÁRIO ===")

ultimo_id += 1
id_usuario = ultimo_id

usuario = input("Usuário: ")
senha = input("Senha: ")

senha_criptografada = hashlib.md5(senha.encode()).hexdigest()

confirmar_senha = input("Confirmar senha: ")
confirmar_criptografada = hashlib.md5(confirmar_senha.encode()).hexdigest()

if senha_criptografada == confirmar_criptografada:
    usuarios.append({
        'id': id_usuario,
        'usuario': usuario,
        'senha': senha_criptografada
    })
    
    print("\n=== CADASTRO REALIZADO COM SUCESSO ===")
    print(f"ID: {id_usuario}")
    print(f"Usuário: {usuario}")
    print(f"Senha criptografada: {senha_criptografada}")
else:
    print("\n❌ Erro: As senhas não coincidem!")
