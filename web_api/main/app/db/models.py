import os
from uuid import uuid4
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class results(Model):
    __keyspace__ = os.getenv('CASSANDRA_KEY_SPACE')
    __table_name__ = 'results'

    id = columns.UUID(primary_key=True, default=uuid4)
    ip = columns.Text(index=True, default=None)
    time = columns.DateTime(default=datetime.utcnow)
    state = columns.Boolean(default=False)

    @classmethod
    def find_by_ip(cls, ip: str):
        return cls.objects(ip=ip)

    @classmethod
    def find_all(cls):
        return cls.objects.all()


class creditcard(Model):
    __keyspace__ = os.getenv('CASSANDRA_KEY_SPACE')
    __table_name__ = 'creditcard'

    id = columns.Integer(primary_key=True)
    Date = columns.DateTime()
    Open = columns.Float()
    High = columns.Float()
    Low = columns.Float()
    Close = columns.Float()
    Volume = columns.Float()
    Ex_Dividend = columns.Float()
    Split_Ratio = columns.Float()
    Adj_Open = columns.Float()
    Adj_High = columns.Float()
    Adj_Low = columns.Float()
    Adj_Close = columns.Float()
    Adj_Volume = columns.Float()
    