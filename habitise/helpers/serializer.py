from django.core import serializers
import json

def serialize_model(model):
    serialized_model = json.loads(serializers.serialize('json', [model, ]))
    organized_serial = {
        "id": serialized_model[0]['pk']
    }
    for field in serialized_model[0]['fields'].keys():
        organized_serial[field] = serialized_model[0]['fields'][field]
    return organized_serial
    
def serialize_models(models):
    serialized_models = json.loads(serializers.serialize('json', models))
    final_result = []
    for model in serialized_models:
        organized_serial = {
        "id": model['pk']
        }
        for field in model['fields'].keys():
            organized_serial[field] = model['fields'][field]
        final_result.append(organized_serial)
    return final_result