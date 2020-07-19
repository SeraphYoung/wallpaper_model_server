import json

import app
from core import generate


def image(request):
    j = json.loads(request.data)
    model = j["model"]
    ct = 0
    for k in app.imageDt:
        print(ct)
        ct += 1
        v = app.imageDt.get(k)
        generate.picture(model, k, v)
