# Projeto do MBA de Engenharia de Dados

## Projeto de previsão de fraude em transações financeiras

Este projeto tem por finalidade compor parte da avalição das disciplinas de Dados E Analytics nas Organizações, Data Lakes, Lakehouses e Datas Meshes, Governança de Daddos e Hands-on Fundamentos de Ddos e Analytics do curso de MBA em Engenharia de Dados.
O projeto consiste em criar um modelo de previsão de fraudes em transações financeira, e, para isso foram realizados os seguintes passos:
- Automação do processo de extração de arquivos CSV disponíveis na plataforma de dados Kaggle;
- Armazenamento do dataset em um datalake no Google Cloud Storage;
- Ingestão do daods em uma tabela no google BigQuery;
- Criação de modelagem dimensional e separação de camadas utilizando o DBT;
- Criação do modelod de previsão de fraudes;
- Dashboard no Power BI.

### Integrantes
| Nome               | Função                                              |
|--------------------|-----------------------------------------------------|
| Fabio Emanoel    | Analista de dados                                    |
| Lais Helena  | Engenheira de Machine Learn                              |
| Neoaquison Medeiros     | Engenheiro de dados e Governaça de dados                                       |
| Tainá Costa    | Product Manager e Analista de dados |

## Arquitetura do Sistema

1. **Cloud Scheduler**: Schedular o job para a coleta de dados.
2. **Cloud Function - Baixador de CSV**: Responsável pelo download do arquivo CSV do Kaggle.
3. **Google Cloud Storage**: Armazena o arquivo CSV baixado no data lake.
4. **Cloud Function - Ingestor de BigQuery**: Lê o arquivo CSV armazenado no Google Cloud Storage e ingere os dados no Google BigQuery para análise.
5. **BigQuery**: Armazena a tabela criada a partir do arquivo no data lake.

## Fluxo de Trabalho
Abaixo segue o desenho da arquitetura. Adicionalmente, a segunda parte do projeto consiste em realizar o tratamento da tabela utilizando o DBT. Os scripts dessa modelagem podem ser encontrados neste [neste ](https://github.com/mackenzie-project/projeto-mackenzie-dbt) repositório

![](./image/Arquitetura%20Neo.png)
