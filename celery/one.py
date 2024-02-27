from celery import Celery
import time
from celery.utils.log import get_task_logger


app = Celery(main="one", broker="amqp://guest:guest@localhost:5672", backend="rpc://")
logger = get_task_logger(__name__)



# @app.task(name="app.adding")
# def add(a, b):
#     time.sleep(15)
#     return a + b 

#########################

@app.task(bind=True, default_retry_delay=600)
def devision(self, a, b):
    try:

        return a / b
    
    except ZeroDivisionError:
        logger.info("Sorry...")
        return self.retry(countdown=10, max_retries=10)