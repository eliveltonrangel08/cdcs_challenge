## Descrição dos artefatos presentes no grupo de atividades A2

Observação importante: por conta do tamanho dos arquivos `.dbc` que foram utilizados para este modelo 
(aprox. 600mb do arquivo zipado), os mesmos serão colocados temporariamente em um [diterório no google drive](https://drive.google.com/file/d/1KDDIrT8I74BqCc2p7unWC9t5ADQfo92w/view?usp=sharing). Outra alternativa é realizar o download dos mesmos dados pelo próprio 
[DATASUS](http://www2.datasus.gov.br/DATASUS/index.php?area=0901), conforme os parâmetros especificados a seguir.

* SIASUS >  
  * Modalidade de Arquivos para Download: `Dados`
  * Tipos de Arquivo: `AM - APAC de Medicamentos - A partir de Jan/2008`
  * Ano: `2020`
  * UF: `Todas`
  * Meses: `Janeiro-Julho`

### Grupo A.2 - Criar tabela(s) no SGDB PostgreSQL e importar os dados, de pelo menos um mês, de todos os estados da federação da APAC de medicamentos.

O modelo relacional proposto possui duas tabelas básicas: `unidade_federativa` e `apac_medicamentos`. A primeira é
responsável por armazenar todas as unidades federativas do Brasil, enquanto a segunda irá armazenar
todos os dados do SIASUS-APAC disponíveis no datasus e presentes no diretório `A1/dbc_files`.

Para a tabela `unidade_federativa`, foram utilizados os mesmos atributos disponíveis na API de consulta
pública do IBGE: `cod_uf, nome, sigla, regiao`. Outra informação adicional é a `população`, disponível em outra API 
pública do IBGE. Este dado é importante para avaliações de estatísticas populacionais, mais precisamente para medir a 
proporção de dados com base na população das unidades federativas, não considerando apenas os dados brutos.

Para a tabela `apac_medicamentos`, foram utilizados os mesmos atributos disponíveis nos arquivos `.dbc`, além de uma
coluna de chave extrangeira referenciando à tabela `unidade_federativa`.

O diagrama UML do banco de dados proposto pode ser visto no diretório `A2/artifacts/DATABASE:cdcs_challenge.png/.uml`

### Gerando o script SQL/DDL para criação do banco de dados e suas respecitvas tabelas

Para facilitar a criação do arquivo .sql (definição do modelo do banco), foi desenvolvido o script `autogenerate_ddl.py`.
Este script simplismente realiza a leitura de um único arquivo .dbf para recuperar as informações dos nomes das colunas
 para auxiliar na criação da tabela `apac_medicamentos`. Deste modo, basta executar o script que automaticamente o 
arquivo `dll_<db_name>.sql` será gerado e estará pronto para ser executado (ver `README.md` no diretório principal).

Este script também realiza o download do arquivo UF.csv contendo os dados necessários para persistir na tabela de 
`unidade_federativa`. Após a criação do modelo do banco de dados, o sistema realiza uma consulta em uma API pública do 
IBGE e salva esses dados em no arquivo mencionado anteriormente.

### Importando os dados iniciais (unidades federativas) e do APAC medicamentos

OBS.: Para essa etapa funcionar, deve-se antes executar o arquivo `dll_<db_name>.sql` para a construção do modelo do 
banco de dados (ver `README.md` no diretório principal)

Há duas formas de realizar a importação destes dados: executando o script `import_data_to_db.py` (execução única) ou 
através do notebook  `import_data_to_db.ipynb`, ambos executam as mesmas tarefas de forma ordenada.

A primeira coisa realizada pelo script é a importação das unidades federativas. Em seguida, todos os arquivos `.dbf` 
presentes no diretório `A1/dbc_files` são persistidos no banco de dados.

### DUMP do banco de dados

Por conta do tamanho do dump do banco de dados (>500MB), o aquivo está disponível [nest link](https://drive.google.com/file/d/10mNTr11xnjj6iImkF4DHGyoPlBUk6hi8/view?usp=sharing).
