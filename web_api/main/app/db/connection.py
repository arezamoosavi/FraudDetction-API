import os

from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import register_connection, set_default_connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider

__all__ = ['Cassandra']

class Cassandra:
    session = None
    cluster = None

    def __init__(self):
        self.key_space = os.getenv('CASSANDRA_KEY_SPACE')
        self.username = os.getenv('CASSANDRA_USER')
        self.password = os.getenv('CASSANDRA_PASSWORD')
        self.connect()

    def connect(self):
        auth_provider = PlainTextAuthProvider(username=self.username, password=self.password)

        self.cluster = Cluster(
            ['node_0', 'node_1'],
            auth_provider=auth_provider,
            # executor_threads=int(os.getenv('CASSANDRA_EXECUTOR_THREADS')),
            # protocol_version=int(os.getenv('CASSANDRA_PROTOCOL_VERSION')),
        )

        self.session = self.cluster.connect()
        self.session.execute("""
                CREATE KEYSPACE IF NOT EXISTS test_key_space
                WITH REPLICATION =
                { 'class' : 'SimpleStrategy', 'replication_factor': '3'}  
                AND durable_writes = true;
                """)
        self.session.set_keyspace(self.key_space)

        register_connection(str(self.session), session=self.session)
        set_default_connection(str(self.session))

    def sync_table(self, database):
        return sync_table(database)

    def disconnect(self):
        self.cluster.shutdown()