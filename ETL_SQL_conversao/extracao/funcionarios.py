import sys
import os
import pandas as pd
import logging
from datetime import datetime
from sqlalchemy import text

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conect.conexao import conexao_bd1
from sql.extracao_funcionarios import SELECT_FUNC, MAPEAMENTO_COLUNAS, TABELA_DESTINO

# --- CONFIGURAÇÃO DE PASTAS PARA ORGANIZAR ---
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, "../arquivos/logs")
out_dir = os.path.join(base_dir, "../arquivos/data_out")

for folder in [log_dir, out_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- CONFIGURAÇÃO DE LOG DETERMINA NOME E DESCRIÇÕES---
log_file = os.path.join(log_dir, f"extracao_Funcionarios{datetime.now().strftime('%Y%m%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)


def executar_migracao():
    engine = conexao_bd1()
    agora = datetime.now().strftime('%Y%m%d_%H%M%S')
    logging.info(f" Iniciando extração para a tabela: {TABELA_DESTINO}")

    try:
        # 1. Extração
        df = pd.read_sql(text(SELECT_FUNC), engine)

        if df.empty:
            logging.warning("O banco não retornou nenhum dado para a query informada.")
            return

        # 2. Transformação
        df_final = df.rename(columns=MAPEAMENTO_COLUNAS)

        if 'nomecolabrador' in df_final.columns:
            df_final['nomecolabrador'] = df_final['nomecolabrador'].str.strip().str.title()
            logging.info(" Limpeza de nomes (Title Case) aplicada.")

        # Filtrar apenas as colunas desejadas
        colunas_finais = list(MAPEAMENTO_COLUNAS.values())
        df_final = df_final[colunas_finais]

        # --- ETAPA NOVA: EXPORTAÇÃO PARA ARQUIVO ---
        # Criando o arquivo CSV para auditoria
        nome_arquivo = f"backup_{TABELA_DESTINO}_{agora}.csv"
        caminho_arquivo = os.path.join(out_dir, nome_arquivo)

        # sep=';' facilita abrir direto no Excel sem configurar nada
        df_final.to_csv(caminho_arquivo, index=False, sep=';', encoding='utf-8-sig')
        logging.info(f" Arquivo de evidência gerado em: {caminho_arquivo}")

        # 3. Carga no Banco
        df_final.to_sql(TABELA_DESTINO, engine, if_exists='append', index=False)
        logging.info(f" SUCESSO: {len(df_final)} migração efetuada com sucesso.")

    except Exception as e:
        logging.error(f"X ERRO na extração: {str(e)}")


if __name__ == "__main__":
    executar_migracao()