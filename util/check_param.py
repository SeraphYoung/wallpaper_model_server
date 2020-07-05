valid_model = ["pointarray"]


def validate_model(model):
    if not isinstance(model, str):
        return False, "model should be string"
    if model not in valid_model:
        return False, "not exist model"
    return True, ''


def validate_vector(vector):
    if not (isinstance(vector, list) and len(vector) == 3):
        return False, 'wrong type of matrix, should be 3 * 3 matrix'
    return True, ''
