# -test-o-parser
pull project from https://github.com/userksv/-test-o-parser.git
$ pip install -r requirements.txt
$ docker run -d -p 6379:6379 redis
$ manage.py bot
$ manage.py runserver

endpoints: 
Use httpie 
    http POST localhost:8000/v1/products/ products_count=10
    http GET localhost:8000/v1/products/{product_id}/
    http GET localhost:8000/v1/products/