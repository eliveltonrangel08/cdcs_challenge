### GRUPO-A. Avaliar dados do SIASUS-APAC (pré-requisito)

#### A-1. Analisar a estrutura dos arquivos de disseminação da APAC (em DBC) de medicamentos e definir modelo de dados relacional que considere mais apropriado.

Este diretório armazena os arquivos compactados do datasus (`.dbc`) e possui algumas ferramentas básicas 
para trabalhar com estes arquivos, conforme detalhado a seguir:

* Arquivo `dbc2dbf.sh`:
    * Script para conversão do formato compactado `.dbc` para o arquivo 'descompactado' `.dbf`, necessário para
    a  leitura dos dados por ferramentas do python. Este script utiliza a ferramenta `blast-dbf`, disponível 
      [neste link do github](https://github.com/eaglebh/blast-dbf).
* Arquivo `dbf2csv.py`:
    * Script para conversão dos arquivos `.dbf` para o formato `.csv`, que também podem ser utilizados
    para a leitura dos dados por ferramentas do python. Este script é opcional.
