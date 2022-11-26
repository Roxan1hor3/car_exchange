from rest_framework.renderers import JSONRenderer

from car_exchange_app.models import Car, Message


class CarRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'count': len(data),
            'data': data
        }
        return super(CarRenderer, self).render(response, accepted_media_type, renderer_context)


class MessageRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'count': len(data),
            'data': data
        }
        return super(MessageRenderer, self).render(response, accepted_media_type, renderer_context)
