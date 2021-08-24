import os
from http.client import HTTPException

import pandas as pd
from flask import Flask
from A2.import_data_to_db import DBConnection
app = Flask(__name__)


@app.route('/<cid>')
def get_registers_by_cid(cid):
    db_conn = DBConnection(host=os.environ.get('PG_HOST'),
                           db=os.environ.get('PG_DB'),
                           usr=os.environ.get('PG_USER'),
                           pwd=os.environ.get('PG_PASSWORD'))

    query = f"SELECT am.*, uf.uf_nome, uf.uf_sigla FROM apac_medicamentos AS am INNER JOIN unidade_federativa uf ON uf.uf_cod = am.uf_id " \
            f"WHERE am.ap_cidpri = '{cid}' LIMIT 20;"
    try:

        resp = pd.read_sql_query(query, db_conn._db)
        if resp.empty:
            raise HTTPException(400, 'Não foram encontrados resultados com o CID informado')
        return resp.to_json(orient='records')
    except Exception as e:
        raise HTTPException(400, 'Ocorreu um erro na consulta com o banco de dados: ', e)

@app.route('/')
def hello_world():
    return 'REST Api APAC-Medicamentos!\n\n' \
           'Para consultar algum registro basta informar na URL o CID 10 relativo.\n' \
           'Ex.: http://127.0.0.1:5000/F200'


if __name__ == '__main__':
    app.run()
