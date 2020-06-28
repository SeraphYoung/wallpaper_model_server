import numpy as np
import time
import matplotlib.pyplot as plt

import base64
import cv2


def __project(points, rotateM):
    projected = np.zeros([points.shape[0], 3], dtype=int)
    pic = np.zeros((1920, 1080, 4))
    for i in range(points.shape[0]):
        projected[i][:3] = rotateM.dot(points[i][:3])
        x, y, z = projected[i][0], -projected[i][1], projected[i][2]
        if -960 <= y < 960 and -540 <= x < 540:
            if pic[y + 960][x + 540][3] == 0:
                pic[y + 960][x + 540][3] = z
                pic[int(y) + 960][int(x) + 540][:3] = points[i][3:6] / 255
            elif pic[y + 960][x + 540][3] < z:
                pic[y + 960][x + 540][3] = z
                pic[int(y) + 960][int(x) + 540][:3] = points[i][3:6] / 255
    retval, buffer = cv2.imencode('.png', pic[:, :, :3])
    pic_str = base64.b64encode(buffer)
    pic_str = pic_str.decode()

    plt.imshow(pic[:, :, :3], interpolation='gaussian')
    plt.axis('off')
    plt.savefig("test.png")
    return "data:image/png;base64,"+pic_str


def picture(model, phone_to_world_matrix):
    path = "model/"+model
    pointarray = np.load(path)

    # find the front of the object
    matrix = np.array([[0, 1000, 0], [1000, 0, 0], [0, 0, -1000]])

    # model coordinate to phone coordinate
    m2p = np.array([[0, 1, 0],
                    [-1, 0, 0],
                    [0, 0, -1]])

    # new phone coordinate
    w2p = np.array([[1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0],
                    [0.0, -1.0, 0.0]])

    ###
    # [[0.8660252, -0.0, 0.5000003],
    #  [0.5000003, 0.0, -0.8660252],
    #  [0.0, 1.0, 0.0]]
    ###
    rm = np.array(phone_to_world_matrix)

    # M = (auxi.dot(test.dot(rm))).dot(matrix)
    M = (w2p.dot(rm)).T.dot(m2p.dot(matrix))
    return __project(pointarray, M)
