from util import check_param, response

from core import generate, fetch

import json


def image(request):
    j = json.loads(request.data)
    model = j["model"]
    vector = j["vector"]
    ok, msg = check_param.validate_model(model)
    if not ok:
        return response.illegal_response(400, msg)
    ok, msg = check_param.validate_vector(vector)
    if not ok:
        return response.illegal_response(400, msg)
    return response.success_response(fetch.picture(model, vector))
