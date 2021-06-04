<div align="center"><h1>Producer Consumer Text</h1></div>

## ✒️ Introduction
The application will perform the request json validation and then add this json to a queue to be stored in the output.txt file.

API documentation:
- ReDoc: `/swagger`
- Swagger: `/docs`

Containers:
- `api-producer-consumer-txt`: API that will validate json and send the message to the storage queue
- `worker-producer-consumer-txt`: Worker who will store the messages in the output.txt file

## ⚙️ Environment variables
| Name | Description | Default |
|-|-|-|
|SAVE_LOG|Store logs to file|True|
|BROKER|Connection URL to rabbitmq|N/A|
|BACKEND|Connection URL to the backend that will save the task execution results|N/A|
|VOLUME_PATH_FILE|Absolute path of output.txt file on host|N/A|

Example of exporting environment variables on Linux:
```bash
export SAVE_LOG="False"
export BROKER="amqp://guest:guest@localhost:5672/"
export BACKEND="rpc://"
export VOLUME_PATH_FILE="/home/files"
```

## 📀 Start Application
### Development:
To use the containers in development, use the [docker-compose.dev.yaml](./docker-compose.dev.yaml) file:

```bash
docker-compose -f docker-compose.dev.yaml up -d
```

Check if the `dev-api-producer-consumer-txt`, `dev-worker-producer-consumer-txt` and `dev-rabbitmq` containers are available:
```bash
docker-compose -f docker-compose.dev.yaml ps
```

Expected output:
```text
              Name                            Command               State                             Ports                           
--------------------------------------------------------------------------------------------------------------------------------------
dev-api-producer-consumer-txt      gunicorn -w 3 -b :8000 -k  ...   Up      0.0.0.0:8000->8000/tcp                                    
dev-rabbitmq                       docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:8080->15672/tcp, 15691/tcp, 15692/tcp, 
                                                                            25672/tcp, 4369/tcp, 5671/tcp, 5672/tcp                   
dev-worker-producer-consumer-txt   celery -A producer_consume ...   Up      8000/tcp
```

When making a change in the application, it is necessary to restart the container corresponding to the update. Example:
```bash
docker restart dev-api-producer-consumer-txt 
```

### Production:
Build image:
```bash
docker build -t producer_consumer_txt:0.3.0 .
```

To deploy the containers in production, have a rabbitmq service installed and follow the same steps above using the [docker-compose.yaml](./docker-compose.yaml) file.

The API will be available on `http://localhost:8000`

## 🧪 Run Unit Tests
Install the application package:
```bash
pip3 install .
```

Install pytest:
```bash
pip3 install pytest
```

Run:
```bash
source .env.test
pytest .
```

Expected output:
```text
======================================================== test session starts =========================================================
platform linux -- Python 3.8.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/project
plugins: pylama-7.7.1
collected 3 items                                                                                                                    

tests/unit/test_task.py ...                                                                                                    [100%]

========================================================= 3 passed in 0.20s ==========================================================
```

## 🛠️ Tools Used
<a href="https://docs.python.org/3.8/">Python3.8</a><br>
<a href="https://fastapi.tiangolo.com/">FastAPI</a><br>
<a href="https://gunicorn.org/">Gunicorn</a><br>
<a href="https://github.com/Delgan/loguru">Loguru</a><br>
<a href="https://docs.celeryproject.org/en/stable/">Celery</a><br>
<a href="https://www.rabbitmq.com/">RabbitMQ</a><br>
<a href="https://pylama.readthedocs.io/en/latest/">Pylama</a><br>

## 🧔 Responsible for the project
<p><a href="mailto:bsb.rafaelaraujo@gmail.com">Rafael Araujo</a></p>