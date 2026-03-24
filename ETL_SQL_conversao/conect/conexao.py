import sqlalchemy
from sqlalchemy import create_engine
import urllib.parse


def conexao_bd1():
    """
    Cria a conexão com o banco de dados PostgreSQL usando SQLAlchemy.
    """
    usuario = "postgres"
    senha = urllib.parse.quote_plus("123456")  # Protege caracteres especiais na senha
    host = "localhost"
    porta = "5432"
    banco = "postgres"

    conn_string = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"

    try:
        engine = create_engine(conn_string)

        with engine.connect() as conn:
            pass

        return engine

    except Exception as e:
        print(f"❌ Erro ao conectar no banco de dados: {e}")
        return None


if __name__ == "__main__":
    # Teste isolado da conexão
    teste_engine = conexao_bd1()
    if teste_engine:
        print("✅ Conexão estabelecida com sucesso!")