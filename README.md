# file_converter
Convert files into JPG/PNG files and download them.
30 minutes after convertion, files get automatically deleted.

- Files
- Convertion into PNG/JPG
- Download file

# Requirements

* Python 3.9 and up
* Docker 4.14

# Installation 

1. Create virtual environment:

```
python -m venv venv
```

2. Activate virtual environment
```
.\venv\Scripts\activate
```

3. Install requirements

```
python -m pip install -r requirements.txt
```
4. Create Postgres database.


5. Go to [Djescrety](https://djecrety.ir/) generate secret key and copy it.


6. Create '.env' file in settings root and paste this:

 ```
   root=true
 
   SECRET_KEY=password from Djescrety

   DATABASE_NAME=your_db_name_created

   DATABASE_USER=your_db_user

   DATABASE_PASSWORD=your_password

   DATABASE_HOST=localhost

   DATABASE_PORT=5432
   ```
 7. Run
 
 ```
 docker-compose up --build
 ```
 8. Run
 ```
 docker-compose up
 ```

# Build with
* Django 4
* Docker 4
* Postgres 14
* Celery 5
* Redis 3
