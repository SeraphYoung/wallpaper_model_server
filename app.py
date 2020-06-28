from flask import Flask, request

from api import fetch

app = Flask(__name__)

'''
request:
model: xxx.npy
matrix: 3*3 matrix
'''


@app.route('/fetch', methods=['POST'])
def fetch_image():
    return fetch.image(request)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
