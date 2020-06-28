valid_model = ["pointarray.npy"]


def validate_model(model):
    if not isinstance(model, str):
        return False, "model should be string"
    name = model.split(".")
    if len(name) == 0 or name[1] != "npy":
        return False, "model name are not ended with npy"
    if model not in valid_model:
        return False, "not exist model"
    return True, ''


def validate_matrix(matrix):
    if not (isinstance(matrix, list) and len(matrix) == 3):
        return False, 'wrong type of matrix, should be 3 * 3 matrix'
    for m in matrix:
        if not (isinstance(m, list) and len(m) == 3):
            return False, 'wrong type of matrix, should be 3 * 3 matrix'
    return True, ''
