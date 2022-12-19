import abc


class ClientBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.interval = 0
        self.parallel = 0
        self.initializer = self.init_db
        self.init_args = ()
        self.pool_func = self.concurrent_pool_function
        self.iterable = iter([])

    @abc.abstractmethod
    def init_db(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def concurrent_pool_function(self, *args, **kwargs):
        pass