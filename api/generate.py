import json

import app
from core import generate


def image(request):
    j = json.loads(request.data)
    model = j["model"]
    for k in app.imageDt:
        v = app.imageDt.get(k)
        generate.picture(model, k, v)
