# Build a Find Route Application With Django


You can:

- **Login and Registration** added new user and login to system
- **ADD** new city, routes and train.
- **Update and Delete** city and trains
- **FindRoute** from city, to city, through cities



## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source ./venv/bin/activate
```

Navigate to the folder for the step you're currently on.

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
```

Make and apply the migrations for the project to build your local database:

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

Create a superuser that allows you to log in to your Django admin portal:

```bash
(venv) $ python manage.py createsuperuser
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials. 