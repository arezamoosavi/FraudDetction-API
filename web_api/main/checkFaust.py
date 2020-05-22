import os
import faust
import logging
import asyncio

redis_server = os.environ.get('REDIS_SERVER','redis://redis:6385/0')
kafka_broker = os.environ.get('KAFKA_SERVER', 'kafka://kafka:9092')

app = faust.App(
    'test_app',
    version=1,
    autodiscover=True,
    origin='app',
    broker=kafka_broker,
    store=redis_server,
    key_serializer='json',
    value_serializer='json',
    )

@app.task
async def on_started():
    print('TEST APP STARTED')


logging.basicConfig(filename='faustLogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():
    
    await app.start()
    logging.info('Faust Works')
    await app.stop()
    exit(1)



if __name__ == '__main__':

    try:
        asyncio.get_event_loop().run_until_complete(main())
        
    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)

