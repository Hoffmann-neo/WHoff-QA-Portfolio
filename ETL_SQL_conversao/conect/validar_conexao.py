from conect.conexao import conexao_bd1

if __name__ == "__main__":
    # Teste isolado da conexão
    teste_engine = conexao_bd1() #alterar a conexao necessaria
    if teste_engine:
        print("✅ Conexão estabelecida com sucesso!")