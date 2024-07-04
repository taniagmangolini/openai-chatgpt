from api import client
from pprint import pprint


models = client.models.list()
for model in models:
    print(model.id)