from app import directionMatch


def picture(model, vector):
    key = ','.join([str(a) for a in vector])
    d = directionMatch[key]
    value = ','.join([str(a) for a in d])
    path = "static/"+model+"/"+value+'.png'
    return path
