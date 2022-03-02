from django.urls import register_converter

class MonConvert:
    regex = r'\d\d'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

register_converter(MonConvert, 'hometype')