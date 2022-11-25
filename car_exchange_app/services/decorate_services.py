def only_objects_decorator(func: callable):
    def only_objects_wrapper(objects, only=(), *args, **kwargs):
        return func(objects, *args, **kwargs).only(*only)

    return only_objects_wrapper


def select_related_objects_decorator(func: callable):
    def select_related_objects_wrapper(objects, select_related=(), *args, **kwargs):
        return func(objects, *args, **kwargs).select_related(*select_related)

    return select_related_objects_wrapper


def prefetch_related_objects_decorator(func: callable):
    def prefetch_related_objects_wrapper(objects, prefetch_related=(), *args, **kwargs):
        return func(objects, *args, **kwargs).prefetch_related(*prefetch_related)

    return prefetch_related_objects_wrapper


def defer_objects_decorator(func: callable):
    def defer_objects_wrapper(objects, defer=(), *args, **kwargs):
        return func(objects, *args, **kwargs).defer(*defer)

    return defer_objects_wrapper
