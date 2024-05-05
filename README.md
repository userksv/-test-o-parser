# -test-o-parser
pull project from https://github.com/userksv/-test-o-parser.git
$ pip install -r requirements.txt
$ docker run -d -p 6379:6379 redis
$ manage.py bot
$ manage.py runserver
$ celery -A test_project worker --loglevel=INFO

endpoints: 
Use httpie 
    http POST localhost:8000/v1/products/ products_count=10
    http GET localhost:8000/v1/products/{product_id}/
    http GET localhost:8000/v1/products/


    ## Project Setup

1. Clone the project repository:
    ```bash
    git clone https://github.com/userksv/-test-o-parser.git
    ```

2. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run Redis Docker container:
    ```bash
    docker run -d -p 6379:6379 redis
    ```

4. Run the bot:
    ```bash
    python manage.py bot
    ```

5. Start the Django server:
    ```bash
    python manage.py runserver
    ```

6. Run Celery worker:
    ```bash
    celery -A test_project worker --loglevel=INFO
    ```

## Endpoints

Use [HTTPie](https://httpie.io/) to interact with the API.

### Create Products

```bash
http POST localhost:8000/v1/products/ products_count=10
