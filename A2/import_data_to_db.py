import psycopg2
import os
import pandas as pd
from simpledbf import Dbf5
import re
import multiprocessing
from threading import Thread


class DBConnection(object):
    _db = None

    def __init__(self, host, db, usr, pwd):
        self._db = psycopg2.connect(host=host,
                                    user=usr,
                                    password=pwd,
                                    database=db)

    def close_connection(self):
        self._db.close()

    def dml(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except Exception as e:
            print(f"SQLException dml: {e}")
            return False

    def dml_many(self, sql, tpls):
        try:
            cur = self._db.cursor()
            cur.executemany(sql, tpls)
            cur.close()
            self._db.commit()
        except Exception as e:
            print(f"SQLException dml: {e}")
            return False

    def query(self, sql):
        rs = None
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
        except Exception as e:
            print(f"SQLException query: {e}")
            return False
        return rs


def check_env_vars():
    envars = ['PG_HOST', 'PG_USER', 'PG_PASSWORD', 'PG_DB']

    for var in envars:
        if not os.environ.get(var, None):
            raise Exception(f"Environment variable not set: {var}\nPlease run 'export $(cat .env)' in the root dir.")


def get_uf_code(fname):
    fsplit = fname.split('.dbf')[0]
    ds, state, year, month = re.findall('..', fsplit)
    # sigla = ufs[ufs.uf_sigla == initials]
    sigla = ufs.query(f'uf_sigla == "{state}"')
    return sigla['uf_cod']


def dbf_file_2_dataframe(filename):
    dbf = Dbf5(f'{f_path}/{filename}', codec='latin')
    df = dbf.to_dataframe()
    return df


def persist_data_in_db(filename):
    print(f"Reading {filename} data (dbf to dataframe)...")
    df = dbf_file_2_dataframe(f"{filename}")
    initials = get_uf_code(filename).iloc[0]
    df['UF_ID'] = initials
    tpls = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    values_refs = ','.join(['%s' for x in range(len(df.columns))])
    print(f"making insert into script from {filename}...")
    sql = f"INSERT INTO apac_medicamentos ({cols}) VALUES ({values_refs})"
    print(f"Inserting data from {filename}...")
    db_conn.dml_many(sql, tpls)


def get_ufs():
    ufs = db_conn.query("select * from unidade_federativa;")

    if not len(ufs):
        df = pd.read_csv('UF.csv')
        if len(df):
            for i, j in df.iterrows():
                try:
                    sql = f"INSERT INTO unidade_federativa values ({j['UF_COD']}, '{j['UF_NOME']}', '{j['UF_SIGLA']}', '{j['UF_REGIAO']}');"
                    db_conn.dml(sql)
                except Exception as e:
                    print(f"SQLException: {e}")

    ufs_query = pd.read_sql_query("select * from unidade_federativa", db_conn._db)
    return pd.DataFrame(ufs_query)


if __name__ == '__main__':
    check_env_vars()
    f_path = '../A1/dbc_files'

    db_conn = DBConnection(host=os.environ['PG_HOST'],
                           db=os.environ['PG_DB'],
                           usr=os.environ['PG_USER'],
                           pwd=os.environ['PG_PASSWORD'])

    ufs = get_ufs()
    f_names = [file for file in os.listdir(f_path) if file.endswith('.dbf')]
    count = 1
    for f_name in f_names:
        print(f"Starting process {count} of {len(f_names)}")
        Thread(target=persist_data_in_db(f_name)).start()
        count += 1
