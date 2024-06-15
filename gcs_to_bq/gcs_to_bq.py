import functions_framework
import csv
from google.cloud import storage, bigquery
from google.cloud.exceptions import NotFound

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def upload_csv_to_bigquery(cloud_eventt):
    bucket_name = 'mk-datalake'
    file_name = 'file/fraud_detection_dataset.csv'
    ignore_header=True
    dataset_id = 'transactions'
    table_id = 'financial_transaction'

    storage_client = storage.Client()
    bq_client = bigquery.Client()

    table_ref = f'{bq_client.project}.{dataset_id}.{table_id}'

    # Esquema da tabela no BQ
    schema = [
        bigquery.SchemaField('Transaction_ID', 'STRING'),	
        bigquery.SchemaField('Customer_Name',	'STRING'),	
        bigquery.SchemaField('Customer_Email','STRING'),	
        bigquery.SchemaField('Transaction_Amount', 'FLOAT'),	
        bigquery.SchemaField('Transaction_Date', 'DATE'),	
        bigquery.SchemaField('Merchant_Name', 'STRING'),	
        bigquery.SchemaField('Merchant_Email', 'STRING'),	
        bigquery.SchemaField('Merchant_Location', 'STRING'),	
        bigquery.SchemaField('Card_Number', 'INTEGER'),	
        bigquery.SchemaField('Card_Expiry', 'STRING'),	
        bigquery.SchemaField('Card_CVV', 'INTEGER'),	
        bigquery.SchemaField('IP_Address', 'STRING'),	
        bigquery.SchemaField('Device_Type', 'STRING'),	
        bigquery.SchemaField('Transaction_Type', 'STRING'),	
        bigquery.SchemaField('Fraudulent', 'BOOLEAN')
    ]

    # Verifica se a tabela já existe, se sim,  deleta 
    try:
        bq_client.get_table(table_ref)
        print(f'Tabela {table_ref} já existe. Apagando tabela.')
        bq_client.delete_table(table_ref)
        print(f'Tabela {table_ref} apagada.')
    except NotFound:
        print(f'Tabela {table_ref} não existe.')

    # Cria a tabela no BQ
    table = bigquery.Table(table_ref, schema=schema)
    table = bq_client.create_table(table)
    print(f'Tabela {table_ref} criada no BQ.')

    # Lê o arquivo CSV do GCS
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()

    # Converte o CSV para linhas de dados
    rows = []
    reader = csv.DictReader(content.splitlines())
    
    if ignore_header:
        next(reader, None) 

    for row in reader:
        rows.append(row)

    # Insere os dados no BQ
    errors = bq_client.insert_rows_json(table_ref, rows)
    if not errors:
        print(f'Novas linhas foram adicionadas na tabela {table_ref}.')
    else:
        print(f'Erros encontrados ao tentar inserir linhas: {errors}')
