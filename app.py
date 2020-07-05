from flask import Flask, request

from api import fetch, generate

from util import transform


app = Flask(__name__)


'''
request:
model: xxx.npy
matrix: 3*3 matrix
'''
imageDt = dict()
with open("static/source.txt", 'r') as f:
    lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        s = line.split("-->")
        key = ','.join(transform.toDirection(s[0]))
        value = transform.toMatrix(s[1])
        imageDt[key] = value

directionMatch = dict()
for x in transform.generate_vector():
    v = transform.find_min_cosine(x)
    directionMatch[','.join([str(a) for a in x])] = v


@app.route('/fetch', methods=['POST'])
def fetch_image():
    return fetch.image(request)


@app.route('/generate', methods=['POST'])
def generate_image():
    return generate.image(request)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
