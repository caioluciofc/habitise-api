from django.core import serializers

def serialize_model(model):
    return serializers.serialize('json', [model, ])
    