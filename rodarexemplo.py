import pytest
from database_manager import DatabaseManager, Cliente

#incluir cliente
cliente_novo = Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01")
db_manager = DatabaseManager('meu_banco.db')
resultado_inclusao = db_manager.incluir_cliente(cliente_novo)
print("Resultado da inclusão:", resultado_inclusao)

#verificar cliente
id_cliente = 1
cliente_encontrado = db_manager.verificar_cliente(id_cliente)
if cliente_encontrado:
    print("Cliente encontrado:", cliente_encontrado)
else:
    print("Cliente não encontrado com ID:", id_cliente)

#atualizar cliente
id_cliente_para_atualizar = 1
campo_para_atualizar = "email"  
novo_valor = "newemail@example.com"
resultado_atualizacao = db_manager.atualizar_cliente(id_cliente_para_atualizar, campo_para_atualizar, novo_valor)
if resultado_atualizacao > 0:
    print("Cliente atualizado com sucesso.")
else:
    print("Atualização falhou.")
