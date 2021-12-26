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
- Run the web server: <code>python manage.py runserver</code>, the webapp should be running on localhost with port 8000

## Example

You can find ERP [here](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ERP#R7V3hc6I4FP9rnLn70B0B0fbjauvuzdnbTnfvuvfJSSEqt0icEFvdv%2F4SSBRJUKhQWcKM00KIIXnvlx%2B895JnxxotN58wWC3ukQv9jtl1Nx3rtmOaxsC4pv9YyTYu6fWNuGCOPZdX2hd89X5CXtjlpWvPheFBRYKQT7zVYaGDggA65KAMYIxeD6vNkH941xWYQ6ngqwN8ufTJc8kiLr22u%2Fvyz9CbL8SdjS6%2FsgSiMi8IF8BFrwdFcEPGKCC8iw8QL0EAA0Kv3AP8A%2BKOfbcghI30Y8cc08%2BM1f4wR2juQ7Dywg8OWtJiJ6RVxjOw9Hwm5kRDQ94QvZ1117FGGCESHy03I%2BgzXQk1xH0aZ1zdyQGzdnN8YXT1sp386JLg86v1D7m%2Fnz8Mnq94Ky%2FAX3P5ctmQrRA4dKn8%2BSm9lUe2j9AHxEPB3f7KEAbuR6ZdWunu8SfE6Bu6BwEd%2FDAkAJP9NRTw6mOPds%2B6NUQVft6NrhK8%2FZ48%2BZedfLDF6e0mefF2y89kkfDxhWiNHXhEDmaPQxngOeTf%2FQr%2BeH5C%2BEv%2F0fyMn6yn6dVkdjXgQHEPUMol%2FgmiJaQdohVe99jcIXCRxKUoxJEwXw7RDTgC57sGd%2Fd4QF4ESD6hrR5vh0%2FngYCyaCIeOv9WEh6phnqphvrphmLRSA3Rg8TA90UR%2Bgog0ZSQGEL84jlwyv9LwKTzd8UOCXiOIBihiBOWxeBAKYgAL6CzLYaZg3wfrEIvqh6XLDzfnYAtWhPRkDgbzrwNdB9jvmJ1KYAntLGQY43NfDEt2GXge%2FOAHjsUe%2ByOQwxD2pcJCAmvkYnOF4gJ3ByFE79q3hwqSbBeAm27sgO03XSzgXWgyaJqs04TiNATHTnxgP9InwogmEcqO9QIE6uL0eqbmISsYMUAB%2FHdC4x5OZI9pYoR8hFTbBATSlQtGpw9pB863BHjC5t2YETPjf05%2FbDqmIxQEBIMvEgbkOrpFTJdDQla8fv4cCa6gbkw2fEzIoTSfJZWj8L7tKq5aq2cqrWq0mxP0uzDn0V0i%2BhYZ37E%2BgvPdWEQz0j2UgD2%2BlaoUin%2FnczTykjPw5z6sHLrI6EAq6D8eWN7qRRuDfgU%2BwEgcIjWgRtWQby2pGdafWR2Pnbj58NfX76xv39PJp3dm1OdACCIN647DFfA8YL5JP5mP4UQuwqEbDqZM9YsFTG5mnsHyPR1Jn31i2Y5pN%2B%2FNOkPztLsO834nNLv55Z%2B0yn%2BWtJqAJYwKsHOAuDf7O7vKaavndJP0nzpqNCO1m9aWq%2BG1m8uTevCedcIXr%2FJLf6m87ohu%2B9WOHKVdF3oeEvg11DLZRF5fhg0mciVTkrZdNeSyCVo5OX2TCI3zHdkcqVqZWu9hlM8l%2FizkdtoIlcOWzaoXRg62FuxMAu9QOVIaqjnnFReIhC0o%2FLzDPKWyrOpPG%2FspDIql63ycR0d7G%2BfwwM9yVw2ox16vznC2yn9ntkVAdR6qblCLs%2FAQZO5XG2uycHSVIx7isLpygdkhvAyEyMax7vNQd6Ad3WuFK2NqwIRViN%2FAK0uIW9Dtq6aFPPeQbf1nBmyxdVGvQtiRL%2Fnd2uMVUX9Fw98GyprzCii3noFSXZYbbnekA0y8bq9t8f0CH4XQEWT2V1ppZpaL2U9z9UWE34t4t9q3cpG2%2FjPZkVOzAwVNIjd1eOWbTYUCh9K0wi%2BTGA0meDV8YBs95tw0GYiQyOf226xECfvawVA%2BgqN7nY0lf5urmBvjZ7MRTaZlOJyUym3MrtLQd9NcrmZrcttJwqly031dNbJ31YAIEce2OUCpjaIaf1tVfG%2Byt%2F2vrwv%2B9tqOOvzyr91tu1EoVj9sA6pdCGe6rvppABAmszySvtUsTdhvxqiYYshTtjvxyFhv3Xzf78EElerLkf6kOY%2BoHOr9Qjsa7EWQt0%2FU9LtL2SYvUkjzX9kq8ct%2B8W0WAtRJkaa7ExVC0Jrn9x5oZoT1P%2BeayHU%2FWv4JiND011GikVvKpOsdpquMDiWBQX9%2BLz1tVXF5xdf%2FaBY21bDWX6G%2FDXdaKRY2Kb7ttEsKGjH56IbLZ%2BXzueXTwJgnud3qz2hmxkKaDqhCzUmPTHhdIYh6%2B4zQn6nGfGSMjGhHbNbMkgkJBzk7Paf0WsyVXfkDYsjJQYd9HBBliIR90EWbwqArCTeSxC4XyJ8YDZO6HL9w41HvieOE2m76dk%2Bazc7EUm7d8m%2Bjc4bkn2nEnGfzP59NI5xMvt3jkW2lWb7tsViPBElsFP4y5vtu59qyEw3VF62bzWIc5ibFwPxWdnn8wAyibMj%2BzQuh7P0vusb%2B20wS7fTM%2BxcMKNKAttENf4Smd3fQQrO3Iea1S%2B7X7C%2BrZ4u%2B1kR97jcOSKbdxi%2BeCG17abiIPMdQKO4uASyvO%2FnpWTFV2cv0tr6Oi8MG8O%2BvoHxnmx8NTww3tPUHOspzLE2MF4MI9qZZ712G2lV1H%2FxwHjvvEUPtfe79TTdQ9qTFzwAh8dQori40ZSVymWiQj9qb3%2F3pCpqv3iMvPcL%2FfLJmyZxX1Nql9c%2BEC9a8%2BTS%2B%2FJDbZk9AxT6MXv70ydVMfvlo%2BXiZo2l9gwFNJ3abdkRRzkd0JL%2FwujVXVtazwCEdrRuyw68ltZLovWLp8%2B3ZUdbw%2FLnx%2FDVkNhlN9s6hDhK5lU79VbI41n6bxCP01OMEElWx2C1uEcuZDX%2BBw%3D%3D)

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

User activities such as viewing a specific service, searching, filtering will be saved into <code>revision_revision</code> table, by running task with Celery.
