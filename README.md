# file_converter
Convert files into JPG/PNG files and download them.
30 minutes after convertion, files get automatically deleted.

- Files
- Convertion into PNG/JPG
- Download file

# Build with
* Django 4
* Docker
* Postgres
* Celery
* Redis

# Requirements

* Python 3.9 and up
* Docker 4.14

# Installation

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
