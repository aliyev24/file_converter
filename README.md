# file_converter
<div align="center" >
 
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white&style=flat-square)
![Celery](https://img.shields.io/badge/-Celery-37814A?logo=celery&logoColor=white&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-3776AB?logo=postgresql&logoColor=white&style=flat-square)
![Redis](https://img.shields.io/badge/-Redis-DC382D?logo=redis&logoColor=white&style=flat-square)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white&style=flat-square)
![HTML](https://img.shields.io/badge/-Html-E34F26?logo=html5&logoColor=white&style=flat-square)

</div>

_ _ _ _ _ _ _ _ _ _ _

Convert files into JPG/PNG files and download them.
30 minutes after convertion, files get automatically deleted.

- Files
- Convertion into PNG/JPG
- Download file

_ _ _ _ _ _ _ _ _ _ _

### Build with
* Django 4
* Docker
* Postgres
* Celery
* Redis

_ _ _ _ _ _ _ _ _ _ _

### Installation

1. Create '.env' file in settings.py root and paste this:

 ```
DEBUG=0
SECRET_KEY=your_secret_key

POSTGRES_NAME=your_postgres_name
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
   ```

2. Create a docker image and run:

```
docker-compose up --build
```
