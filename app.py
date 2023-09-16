from flask import Flask, jsonify, send_file
from flask_cors import CORS
# import torch


app = Flask(__name__)
CORS(app)  # Enables cross-origin requests

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

trafficJam = {
            "type":"trafficJam",
            "name":"รถติด"
        }

hole = {
            "type":"hole",
            "name":"ถนนขรุขระ"
        }

obstruction = {
            "type":"obstruction",
            "name":"ถนนมีสิ่งกีดขวาง"
        }


def detect1():
    placeholder1 = []
    placeholder1.append(hole)
    placeholder1.append(obstruction)
    return placeholder1

def detect2():
    placeholder2 = []
    placeholder2.append(hole)
    placeholder2.append(obstruction)
    return placeholder2

@app.route('/')
def index():
    return 'Index Page'

@app.route('/result/text/1', methods = ['GET'])
def get_text1():
    text1 = []

    detect1(text1)

    data = {
        "result":[text1]
    }

    # Convert the dictionary to JSON and return it as a response
    return jsonify(data)

@app.route('/result/text/2', methods = ['GET'])
def get_text2():
    text2 = []

    detect2(text2)

    data = {
        "result":[text2]
    }

    # Convert the dictionary to JSON and return it as a response
    return jsonify(data)

@app.route('/result/vdo/1', methods = ['GET'])
def get_video1():
    # Replace 'video.mp4' with the path to your video file
    video_path = 'vdo/chidlom.mp4'
    return send_file(video_path, as_attachment=True)


@app.route('/result/vdo/2', methods = ['GET'])
def get_video2():
    # Replace 'video.mp4' with the path to your video file
    video_path = 'vdo/court.mp4'
    return send_file(video_path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000)
