import pytest
from database_manager import DatabaseManager, Cliente

@pytest.fixture(scope="module")
def db_manager():
    test_db_path = 'users.db'
    manager = DatabaseManager(test_db_path)
    yield manager

@pytest.mark.parametrize("cliente", [
    Cliente("", "invalid_email", "1234567890", "Some Address", "Some City", "ST", "12345-678", "invalid_date", "invalid_date"),
    Cliente("John Doe", "johndoe@example.com", "", "", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01")
])
def test_incluir_cliente_falha_com_dados_invalidos(db_manager, cliente):
    resultado = db_manager.incluir_cliente(cliente)
    assert resultado == "Falha na validação dos dados do cliente."

def test_verificar_cliente_existente(db_manager):
    cliente = db_manager.verificar_cliente(1)  
    assert cliente is not None


def test_verificar_cliente_invalido(db_manager):
    cliente = db_manager.verificar_cliente(9999)  
    assert cliente is None

def test_atualizar_cliente_existente(db_manager):
    resultado = db_manager.atualizar_cliente(1, "nome", "Nome Atualizado")  
    assert resultado > 0
