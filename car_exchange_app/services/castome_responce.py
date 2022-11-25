from rest_framework.renderers import JSONRenderer

from car_exchange_app.models import Car


class CarRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'count': Car.objects.count(),
            'data': data
        }
        return super(CarRenderer, self).render(response, accepted_media_type, renderer_context)
