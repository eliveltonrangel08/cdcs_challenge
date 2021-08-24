## Projeto de desafio para persistência, processamento e análise de dados do SIASUS-APAC

### Conversão de arquivos proprietários/compactados

Antes de começar, é necessário realizar a instalação dos pacotes/bibliotecas necessários(as) para o funcionamento 
adequado deste projeto. Em seguida, é preciso descompactar os arquivos priprietários (.dbc) para arquivos com formatos
acessíveis (`.csv` ou `.dbf`) por ferramentas do python (Pandas, dask, etc). Para isso, execute os passos a seguir:

* Entrar no diretório A1
  
      cd A1
  
* Executar o script para descompressão dos arquivos `.dbc` para `.dbf`
  
      sh dbc2dbf.sh
  
* Opcional*. Caso queira converter os arquivos .dbf para .csv, execute o script em python `dbf2csv.py`
  
      python3 dbf2csv.py
  
    Este procedimento realizará a descompressão dos arquivos compactados para formatos acessíveis (`.dbf` e `.csv`) 
    e irá adicioná-los em um sub diretório `A1/csv`

OBS. Antes de iniciar os demais procedimentos, altere as variáveis de ambiente do arquivo `.env.example` (presente no diretório principal)
para configurar os valores padrões de conexão com o banco de dados PostgreSQL. Renomeie o arquivo para `.env`. Após a configuração das variaveis de ambiente, execute os comandos a seguir (considerando que o diretório atual é o `A1`:

    cd ../
    export $(cat .env)

Após isso, o SO estará com as variáveis de ambientes necessárias para a execução dos scripts.


### Etapa A2: confecção do modelo do banco de dados e importação dos dados

Esta etapa consiste em gerar o arquivo DDL para criação do banco de dados e realizar a importação dos dados presente 
nos arquivos convertidos na etapa anterior. A descrição dos artefatos pode ser visualizada no arquivo 
`artifacts_description.md`, presente no diretório `A2`.

Observação importante*: As variáveis de ambiente precisam estar definidas para que essa etapa funcione corretamente.

* Entrar no diretório A2 (considerando que o diretório atual é o raiz):

      cd A2
* Executar o script para gerar o modelo de banco de dados automaticamente (baseado nas colunas do arquivo `.dbf`):

      python3 autogenerate_ddl.py
* Importar o arquivo `.sql` para a criação do banco e tabelas no PostgreSQL:

      sudo -u postgres PGPASSWORD=${PG_PASSWORD?Variable not set} psql -h localhost -f ddl_${PG_DB?Variable not set}.sql
* Executar o script para importar os dados iniciais (informações sobre as unidades federativas e os dados convertidos 
  na etapa anterior - ver descrição dos artefatos A2):
  
      python3 import_data_to_db


#### Todos os diretórios possuem arquivos `README.md` descrevendo os artefatos e justificativas de alguns grupos.

### Etapa D1

Todas as orienções deste grupo estão no diretório `D1-D2`.