from car_exchange_app.services.decorate_services import select_related_objects_decorator, \
    prefetch_related_objects_decorator, only_objects_decorator, defer_objects_decorator


@defer_objects_decorator
@prefetch_related_objects_decorator
@select_related_objects_decorator
def all_objects(objects):
    return objects.all()


@prefetch_related_objects_decorator
@select_related_objects_decorator
def filter_objects(objects, **kwargs):
    return objects.filter(**kwargs)
