from minio import Minio

minio_client = Minio(
    "localhost:9000",
    secure=False,
    access_key="DBE4933647617",
    secret_key="ABw62bUBlQSXAArP1vsVVWabaSIn5lhs",
)
