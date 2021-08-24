## GRUPO-D. Disseminação

### D-1. Implementar um serviço do tipo REST, em qualquer framework e/ou linguagem de programação, que permita consumir os registros da APAC de medicamentos, a partir de um CID 10 informado pelo usuário no navegador.

Serviço implementado e disponível no arquivo app.py (presente na raiz do projeto)

Para rodar o serviço REST, basta executar o comando a seguir (considerando que o diretório atual é o raiz):

    python -m flask run
Após isso, basta acessar o link gerado, que possivelmente será: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Pra acessar o requisito deste subgrupo, basta acessar a URL apresentada no serviço e adicionar o CID 10 na barra de endereços do navegador. Ex:

    http://127.0.0.1:5000/F200

#### OBS*! Caso apresente algum erro de conexão com o banco de dados, verifique se as variáveis de ambiente estão devidamente definidas (ver README.md na raiz do projeto)

#### OBS2*! Por conta do limite de memória, este serviço só retorna os 20 primeiros registros. Uma alternativa a este problema é acrescentar parâmetros de paginação. Entretanto, por conta das limitações de tempo e de especificações dos requisitos, isto pode ser implementado posteriormente.

### D-2. Que ferramenta de ETL open source você recomendaria para criar fluxos automatizados a partir de um serviço REST? Identificar opções e justificar sua escolha.

Uma ferramenta ETL open source que é bastante viável para logística de dados entre sistemas é a 
[Apache NiFi](https://nifi.apache.org/). Essa ferramenta pode suportar fontes de dados agnósticas e diferentes formatos 
de dados, esquemas, protocolos, etc. Ela possui uma UI baseada na WEB, é altamente configurável e é extensível, podendo 
criar alguns recursos próprios através de sua API.

Outras alternativas seriam o ApacheCamel, Apache Kafka, JasperSoft e o CoverETL.
