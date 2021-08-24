## GRUPO-C. Evolução do modelo

### C-1. Se um dos requisitos fundamentais do sistema fosse a necessidade dos dados coletados pudessem mudar no tempo, sem a necessidade de alterar o modelo de implementação. Que modelagem de dados você proporia? Justifique.

O modelo de dados proposto segue o padrão relacional, conforme requisito do Grupo-A. Uma das 
fraquezas do modelo proposto é a ausência do controle de versionamento de importação, que garantiria que
um determinado arquivo já estaria importado no banco, não necessitando sua reimportação e mantendo os dados sem redundância.
Além disso, o modelo relacional tende a crescer verticalmente. Neste sentido, caso haja alguma mudança na estrutura de 
alguma entidade, como a inclusão de novas colunas, o modelo relacional não é uma opção muito viável. Portanto, a 
utilização de bancos de dados com suporte a modelos não-relacionais, ou NoSQL, tende a ser uma alternativa mais 
indicada [1, 2].

Os bancos de dados NoSQL tentem a ser utilizados em aplicações que podem crescer horizontalmente ou precisam de alto 
desempenho. Conforme descrito por [2], estes bancos foram criados para suprir necessidade no qual os modelos relacionais 
não são eficazes, entre estas a escalabilidade e o crescimento horizontal.

Nesse sentido, caso a estrutura básica das entidades possa mudar com o tempo (crescimento horizontal), então é necessário
adequar o modelo de importação para uma proposta não-relacional, em que os dados podem ser organizados em documentos 
(descritos como dados no formato de chave-valor, a exemplo do JSON), 
colunas, grafos e chave-valor. O MongoDB, Cassandra, Neo4j e o Riak são opções que comportam os quatro tipos de banco 
de dados relacionais, respectivamente.

Uma alternativa que também pode ser viável é o modelo híbrido (relacional + não-relacional), que une o melhor dos dois 
mundos. O PostgreSQL por natureza segue o modelo relacional, mas pode ser utilizado também  como alternativa híbrida, 
utilizando colunas que, ao invés de armazenar um registro relacional, armazena documentos no formato JSON.



### Referências utilizadas:

[1] NoSQL vs SQL Databases
"Nosql Vs SQL Databases ". Mongodb, 2021, https://www.mongodb.com/nosql-explained/nosql-vs-sql. Acessado em 24 Aug 2021.

[2] SQL vs NoSQL, qual usar?
"SQL Vs Nosql, Qual Usar?". Treinaweb.Com.Br, 2021, https://www.treinaweb.com.br/blog/sql-vs-nosql-qual-usar. Acessado em 24 Ago 2021.

### C-2. Definir o novo modelo, caso o modelo proposto em A-1. não seja mais a melhor opção para atender o requisito de C-1.

Conforme especificado na etapa anterior, fazer o uso de modelo híbrido pode ser uma alternativa ao modelo proposto. 
A figura `proposed_model.png` representa um modelo relacional para algumas entidades definidas, juntamente com uma 
coluna (`apac_medicamentos.am_data`) que armazenaria todos os dados presentes nos arquivos `.dbf` utilizados no Grupo-A, 
sem a necessidade de colunas para tais fins. Deste modo, essa solução pode ser viável caso haja a inclusão de uma nova 
coluna nos registros base.

Outra novidade é a inclusão da entidade `controle_importacao`, que tem a finalidade de armazenar metadados para o melhor 
gerenciamento na importação dos arquivos para o banco de dados, garantindo que estes não sejam redundantes 
(importados mais de uma vez) e mantendo a integridade dos mesmos. 