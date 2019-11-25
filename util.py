from functools import partial


def call(func, *args, **kwargs):
    return partial(func, *args, **kwargs)()


def create_collector():
    collection = []

    def collect(node):
        collection.append(node)

    return collect, collection
