*Base on celery with rabbitmq
*Change config/config.py 
*Make sure the broke and backend amqp url is correct and available


Create or renew client folder:
python celery_test_divide.py -renew_c 

Start server:
python celery_test_divide.py -s

Start client:
python celery_test_divide.py -c

