import os
import requests
from simpledbf import Dbf5


def check_env_vars():
    try:
        if not os.environ['PG_DB']:
            raise Exception('Variable not set')
    except Exception as e:
        print(f"Error recovering environment variable: {e}")


def make_sql_file():
    print("Generating SQL file with creation of database and tables...")

    with open(f'ddl_{db_name}.sql', 'w') as f_out:
        f_out.write(f"-- DROP DATABASE {db_name};\n\n")

        f_out.write(f"CREATE DATABASE {db_name}\n"
                    "\t\tWITH\n"
                    "\t\tOWNER = postgres\n"
                    "\t\tENCODING = 'UTF8'\n"
                    "\t\tTABLESPACE = pg_default\n"
                    "\t\tCONNECTION LIMIT = -1;\n\n")

        f_out.write(f"\c {db_name};\n\n")

        f_out.write("CREATE TABLE IF NOT EXISTS public.unidade_federativa(\n"
                    "\t\tUF_COD INT UNIQUE,\n"
                    "\t\tUF_NOME VARCHAR NOT NULL UNIQUE,\n"
                    "\t\tUF_SIGLA VARCHAR(2) NOT NULL UNIQUE,\n"
                    "\t\tUF_REGIAO VARCHAR NOT NULL,\n"
                    "\t\tUF_POPULACAO INT,\n"
                    "\t\tPRIMARY KEY(UF_COD));\n\n")
        f_out.write("CREATE TABLE IF NOT EXISTS public.apac_medicamentos(\n"
                    "\t\tID SERIAL,\n"
                    "\t\tUF_ID INT,\n")

        for column in columns:
            f_out.write(f"\t\t{column} VARCHAR,\n")

        f_out.write("\t\tPRIMARY KEY(ID),\n"
                    "\t\tCONSTRAINT fk_uf FOREIGN KEY(UF_ID) REFERENCES unidade_federativa(UF_COD));\n")

        f_out.close()
        print("SQL File generated successfully!")


def make_uf_file():
    # Download the UF.csv file from IBGE API
    response = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()

    with open('UF.csv', 'w') as fout:
        fout.write('UF_COD,UF_NOME,UF_SIGLA,UF_REGIAO,UF_POPULACAO\n')
        for resp in response:
            population = requests.get(f"https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/{resp.get('id')}").json()
            fout.write(
                f"{resp.get('id', None)},{resp.get('nome', None)},{resp.get('sigla', None)},"
                f"{resp.get('regiao').get('nome')},{population.get('projecao').get('populacao')}\n")
        fout.close()


if __name__ == '__main__':
    f_path = '../A1/dbc_files'
    f_names = [file for file in os.listdir(f_path) if file.endswith('.dbf')]

    if not len(f_names):
        raise Exception("Error in load file list name")

    dbf = Dbf5(f'{f_path}/{f_names[0]}', codec='latin')
    df = dbf.to_dataframe()
    columns = df.columns

    check_env_vars()
    db_name = os.environ['PG_DB']

    make_sql_file()
    make_uf_file()
