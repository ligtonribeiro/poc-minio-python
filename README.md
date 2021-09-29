## Prova de conceito upload de arquivos usando MinIO

### Instalação:
1. Criar e ativar uma virtualenv

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Instalar pacote MinIO via PIP
```sh
$ pip install minio
```

3. Com Docker e Docker Compose instalado, executar o seguinte comando:
```sh
$ docker-compose up -d
```
