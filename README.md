# Backend code for travel form
Backend is created using Django and has two request types on the route **/forms**. One can make a POST to add data to the database and a GET to fetch all the available submissions from the database

## Steps to run the project
### Create a local postgres database instance
Note the username and password of this instance

### Create a local.env file on the root directory with these secrets
```
export RDS_PASSWORD=<Your DB password>
export RDS_HOSTNAME=127.0.0.1
export RDS_PORT=5432
export RDS_DB_NAME=<Your DB name>
```


### Set up a Python 3.x virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Or otherwise, you can set up a virtual environment from your IDE.

### Source the environment file
```source local.env```

### Install development requirements

```
pip install -r requirements/requirements.txt
```

### Run migrations

```
python manage.py migrate
```

### Run the development server

```
python manage.py runserver

```

You can now run the frontend code and check the complete product there.
