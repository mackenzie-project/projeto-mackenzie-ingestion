import functions_framework
import os
import json
import zipfile
import pandas as pd
from google.cloud import storage

@functions_framework.http
def file_to_gcs(http):
   
    dataset_name = "smmmmmmmmmmmm/fraud-detection-financial-transactions"
    z_file = './fraud-detection-financial-transactions.zip'
    csv_file = 'fraud_detection_dataset.csv'
    gcs_bucket_name = 'mk-datalake'
    gcs_blob_name = 'file/fraud_detection_dataset.csv'
    local_dir = '.'

    unzip_file(dataset_name, z_file)
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(gcs_bucket_name)
        blob = bucket.blob(gcs_blob_name)
        blob.upload_from_filename(os.path.join(local_dir, csv_file))

        print(f"Arquivo {csv_file} carregado para {gcs_bucket_name} como {gcs_blob_name}.")
    except Exception as e:
        print(f"Erro para carregar o arquivo no GCS: {e}")

    return {"message": "Operação concluída com sucesso"}, 200

def download_dataset(dataset_name):
    command = f"kaggle datasets download -d {dataset_name}"
    try:
        os.system(command)
    except Exception as e:
        print(f"Falha ao tentar realizar o download: {e}")
    print('dowload zip realizado')

def unzip_file(dataset_name, zip_path, extract_to='.'):
    download_dataset(dataset_name)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except FileNotFoundError as e:
        print(f"Erro ao extrair o csv: {e}")
    print('csv extraido')
