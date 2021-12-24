# GeoHub

## _Code structure_

Using the basic structure of a Django project, from root directory we have:

- <code>geohub</code>: project root directory, almost project level setting here
- <code>service</code>: service app, the main business lays in here, with all standard elements: model, view, some thing else: task, filter, serializer, unit tests...
- <code>revision</code>: an app for tracking user behavior
- We have something further: docker-compose.yml, requirements.txt, setup.cfg...

## _Steps to setup_

After clone this repo

- Activate virtual env: <code>python3 -m venv venv && source venv/bin/activate</code>
- Install dependent packages: <code>pip install -r requirements.txt</code>
- Run Redis as Celery's task queue with <code>docker-compose up -d</code>
- You need to run Celery for tracking task: <code> celery -A geohub worker -l INFO</code>
- Run the web server: <code>python manage.py runserver</code>

## Example

This repo is shipped with a sqlite3 database for testing purpose. Some examples:

- Get list services: <code>curl http://127.0.0.1:8000/service</code>

```[
    {
        "id": 1,
        "name": "sv1",
        "price": "10.00",
        "description": "askkskd",
        "category": 2,
        "os_platform": [
            1,
            2
        ]
    },
    {
        "id": 2,
        "name": "sv2",
        "price": "100.00",
        "description": "ashdhshd",
        "category": 1,
        "os_platform": [
            2
        ]
    }
]
```

- Search by name: <code>curl http://127.0.0.1:8000/service?search=sv1</code>

```
[
    {
        "id": 1,
        "name": "sv1",
        "price": "10.00",
        "description": "askkskd",
        "category": 2,
        "os_platform": [
            1,
            2
        ]
    }
]
```

- Filter by price: <code>curl http://127.0.0.1:8000/service?price__lt=50&price__gt=1</code>

```
[
    {
        "id": 1,
        "name": "sv1",
        "price": "10.00",
        "description": "askkskd",
        "category": 2,
        "os_platform": [
            1,
            2
        ]
    }
]
```

- Filter by OS: <code>curl http://127.0.0.1:8000/service?os_platform=ubuntu</code>

```
[
    {
        "id": 1,
        "name": "sv1",
        "price": "10.00",
        "description": "askkskd",
        "category": 2,
        "os_platform": [
            1,
            2
        ]
    }
]
```

- Order by name (desc): <code>http://127.0.0.1:8000/service?ordering=-name</code>

```
[
    {
        "id": 2,
        "name": "sv2",
        "price": "100.00",
        "description": "ashdhshd",
        "category": 1,
        "os_platform": [
            2
        ]
    },
    {
        "id": 1,
        "name": "sv1",
        "price": "10.00",
        "description": "askkskd",
        "category": 2,
        "os_platform": [
            1,
            2
        ]
    }
]
```

- Retrive an object: <code>http://127.0.0.1:8000/service/1</code>

```
{
    "id": 2,
    "name": "sv2",
    "price": "100.00",
    "description": "ashdhshd",
    "category": 1,
    "os_platform": [
        2
    ]
}
```

Also support filter by category, support free OS or not, filter by name,...

# User behavior tracking

User activities such as view a specific service, searching, filtering will be saved into <code>revision_revision</code> table, by running task with Celery.
