from util import check_param, response

from core import generate

import json


def image(request):
    j = json.loads(request.data)
    model = j["model"]
    matrix = j["matrix"]
    print(model)
    print(matrix)
    ok, msg = check_param.validate_model(model)
    if not ok:
        return response.illegal_response(400, msg)
    ok, msg = check_param.validate_matrix(matrix)
    if not ok:
        return response.illegal_response(400, msg)
    return response.success_response(generate.picture(model, matrix))
