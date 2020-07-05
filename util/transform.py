import numpy
import app


def toDirection(s):
    s = s.replace(' ', '')
    d = list()
    for a in s.split(","):
        d.append(a)
    return d


def toMatrix(s):
    s = s.replace(' ', '')
    s = s.replace('[', '')
    s = s.replace(']', '')
    d = list()
    count = 0
    temp = list()
    for a in s.split(","):
        temp.append(float(a))
        count += 1
        if count == 3:
            count = 0
            d.append(temp)
            temp = list()
    return d


def generate_vector():
    v = list()
    for i in [x / 10 for x in list(range(-10, 11))]:
        for j in [x / 10 for x in list(range(-10, 11))]:
            for k in [x / 10 for x in list(range(-10, 11))]:
                v.append([i, j, k])
    return v


def cal_cosine(a, b):
    a_dot_b = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    len_a = numpy.sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])
    len_b = numpy.sqrt(b[0] * b[0] + b[1] * b[1] + b[2] * b[2])
    if len_a == 0 or len_b == 0:
        return 0
    return a_dot_b / float(len_a * len_b)


def find_min_cosine(a):
    min_cosine = 1
    min_vector = [-1, -1, -1]
    for v in app.imageDt:
        v = [float(x) for x in toDirection(v)]
        cos = cal_cosine(a, v)
        if cos <= min_cosine:
            min_cosine = cos
            min_vector = v
    return min_vector
