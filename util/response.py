def illegal_response(code, msg):
    return {
        "code": code,
        "msg": msg,
        "data": None
    }


def success_response(data):
    return {
        "code": 0,
        "msg": '',
        "data": data
    }
