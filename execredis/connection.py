from redis import ConnectionPool, StrictRedis


class ExecRedisClients(StrictRedis):
    def __init__(self, host, db, **kwargs):
        super(ExecRedisClients, self).__init__({**dict(
            connection_pool=ConnectionPool(host=host, db=db),
            decode_responses=True), **kwargs}
        )
