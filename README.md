### Set up a Python 3.x virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Or otherwise, you can set up a virtual environment from your IDE.

### Install development requirements

```
pip install -r requirements/development.txt
```

### Set up pre-commit hook

```
pre-commit install
```

### Run migrations

```
python manage.py migrate
```

### Run the development server

```
python manage.py runserver

```

### Run cron jobs locally

Install Redis Server locally and then run the following commands in three different shell environments with all the
environment variables exported:

```
redis-server
celery -A config.celery:app worker -l INFO
celery -A config.celery:app beat --loglevel=INFO
```