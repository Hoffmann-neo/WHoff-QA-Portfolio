
SELECT_FUNC = """
    SELECT 
         f.codigofuncpessoa
        ,fun.codigoempresa
        ,fun.codigofunccontr
        ,fun.nomefunc
    FROM funcpessoa f 
    JOIN funcionario fun ON f.codigofuncpessoa = fun.codigofuncpessoa
"""

MAPEAMENTO_COLUNAS = {
    'codigofuncpessoa': 'codigoFunc',
    'codigoempresa':    'codempresa',
    'codigofunccontr':  'fucionarion',
    'nomefunc':         'nomecolabrador'
}

TABELA_DESTINO = "funcionarios"