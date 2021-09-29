from conf_minio import minio_client
from minio.error import InvalidResponseError

Patientdb = {
    "id": 1,
    "name": "Wellington",
    "bucket_name": "000111222334"
}


def create_bucket_and_upload_file_patient(bucket_name, filename, filepath):
    """ Mock da busca do banco de dados"""
    patient = 1
    bucket_patient = bucket_name

    if patient in Patientdb.values():
        if not bucket_patient == Patientdb['bucket_name']:
            try:
                minio_client.make_bucket(bucket_patient)
                print(f"Bucket {bucket_patient}, criado com sucesso!")
                obj = minio_client.fput_object(
                    bucket_patient, filename, filepath)
                print("Arquivo {0} adicionado com sucesso".format(
                    obj.object_name
                ))
            except IndentationError as err:
                print(err)
        else:
            print(f"Adicionando arquivo ao bucket: {bucket_name}")
            obj = minio_client.fput_object(
                bucket_patient, filename, filepath)
            print("Arquivo {0} adicionado com sucesso".format(
                obj.object_name
            ))
    else:
        print('Usuário não encontrado!!')


create_bucket_and_upload_file_patient('000111222334', 'exame', 'exame.pdf')
