import logging
import asyncio
from app.db.connection import Cassandra


logging.basicConfig(filename='dblogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():

    cassandra = Cassandra()
    await asyncio.sleep(0.001)

    logging.info('Connedted to Cassandra')
    cassandra.disconnect()
    logging.info('dis_connedted to Cassandra')


if __name__ == "__main__":
    
    try:
        asyncio.get_event_loop().run_until_complete(main())
        
        exit(1)

    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)
