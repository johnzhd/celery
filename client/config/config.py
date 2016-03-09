
################################################
### BROKER

BROKER_URL = 'amqp://de:de@193.168.15.173:5672/de'

# using serializer name
# or the actual content-type (MIME)
CELERY_ACCEPT_CONTENT = ['json', 'application/json']

# Random failover strategy
def random_failover_strategy(servers):
    it = list(it)  # don't modify callers list
    shuffle = random.shuffle
    for _ in repeat(None):
        shuffle(it)
        yield it[0]

BROKER_FAILOVER_STRATEGY=random_failover_strategy

BROKER_USE_SSL = False
BROKER_POOL_LIMIT = 10

BROKER_CONNECTION_TIMEOUT = 4

BROKER_CONNECTION_RETRY = True

BROKER_CONNECTION_MAX_RETRIES = 100

######################################
#'''

CELERY_RESULT_BACKEND = 'amqp://de:de@193.168.15.173:5672/de_output'
CELERY_RESULT_EXCHANGE = 'celery'
CELERY_RESULT_EXCHANGE_TYPE = 'direct'
CELERY_RESULT_PERSISTENT = True
CELERY_TASK_RESULT_EXPIRES = 180  

#'''
#####################################

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


####################################
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True




