# -test-o-parser
## Project Setup

1. Clone the project repository:
    ```bash
    git clone https://github.com/userksv/-test-o-parser.git
    ```

2. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run database migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Run Redis Docker container:
    ```bash
    docker run -d -p 6379:6379 redis
    ```

6. Run the bot:
    ```bash
    python manage.py bot
    ```

7. Start the Django server:
    ```bash
    python manage.py runserver
    ```

8. Run Celery worker:
    ```bash
    celery -A test_project worker --loglevel=INFO
    ```

## Endpoints

Use [HTTPie](https://httpie.io/) to interact with the API.

### Create Products

```bash
http POST localhost:8000/v1/products/ products_count=10
```

### Get product by id
```bash
http GET localhost:8000/v1/products/{product_id}/
```

### Get all products
```
http GET localhost:8000/v1/products/
```

## Swagger or ReDoc
```
http://localhost:8000/swagger/
```

contact me at serkimdev@gmail.com