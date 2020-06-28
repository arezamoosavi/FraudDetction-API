import os
from uuid import uuid4
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class result(Model):
    __keyspace__ = os.getenv("CASSANDRA_KEY_SPACE")
    __table_name__ = "result"

    id = columns.UUID(primary_key=True, default=uuid4)
    data = columns.List(value_type=columns.Float)
    is_fraud = columns.Boolean(default=False)
    time = columns.DateTime(default=datetime.utcnow)

    @classmethod
    def find_all(cls):
        return cls.objects.all()

    @classmethod
    def count_all(cls):
        return cls.objects.count()
