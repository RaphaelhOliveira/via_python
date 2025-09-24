test_drives = []
ultimo_id_test_drive = 0

print("=== AGENDAMENTO DE TEST DRIVE ===")

ultimo_id_test_drive += 1
id_test_drive = ultimo_id_test_drive

data_agendamento = input("Data de agendamento (DD/MM/AAAA HH:MM): ")
resultado = input("Resultado: ")

test_drives.append({
    'id': id_test_drive,
    'data_agendamento': data_agendamento,
    'resultado': resultado
})

print("\n=== DADOS CADASTRADOS ===")
print(f"ID: {id_test_drive}")
print(f"Data de agendamento: {data_agendamento}")
print(f"Resultado: {resultado}")
