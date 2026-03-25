
SELECT_FUNC = """
    SELECT
         id_funcionario
         ,codigo_funcionario
         ,nome_completo
         ,cpf
    FROM funcionarios 

"""

MAPEAMENTO_COLUNAS = {
        'id_funcionario': 'codigofunc'
        ,'codigo_funcionario': 'matricula_esocial'
        ,'nome_completo': 'nomecolabrador'
        ,'cpf': 'cpf'
}

TABELA_DESTINO = "funcionarios"