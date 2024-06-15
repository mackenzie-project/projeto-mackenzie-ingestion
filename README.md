# Projeto de Ingestão de Dados utilizando Cloud Scheduler, Cloud Functions, Google Cloud Storage e Google Bigquery

Este projeto tem por finalidade automatizar o processo de extração de arquivos CSV disponíveis na plataforma de dados Kaggle, armazenar o dataset em um datalake no Google Cloud Storage e então, realizar a ingestão desses dados em uma tabela no Google BigQuery para análise.

## Arquitetura do Sistema

1. **Cloud Scheduler**: Schedular o job para a coleta de dados.
2. **Cloud Function - Baixador de CSV**: Responsável pelo download do arquivo CSV do Kaggle.
3. **Google Cloud Storage**: Armazena o arquivo CSV baixado no data lake.
4. **Cloud Function - Ingestor de BigQuery**: Lê o arquivo CSV armazenado no Google Cloud Storage e ingere os dados no Google BigQuery para análise.
5. **BigQuery**: Armazena a tabela criada a partir do arquivo no data lake.

## Fluxo de Trabalho
Abaixo segue o desenho da arquitetura. Adicionalmente, a segunda parte do projeto consiste em realizar o tratamento da tabela utilizando o DBT. Os scripts dessa modelagem podem ser encontrados neste [neste ](https://github.com/mackenzie-project/projeto-mackenzie-dbt) repositório

![](./image/Arquitetura%20Neo.png)
