"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/18
Usage: The main function of the Flask
"""

from flask import Flask, render_template, request
from utils.detection import detection
from utils.analysis import analysis
from utils.encoder import encoder
from utils.get_image import get_image
from utils import generate_unique_id
import json

app = Flask(__name__)

@app.route('/detect', methods=['post', 'get'])
def detect():
    get_image()

    min_threshold = float(request.values.get('threshold'))

    output_dict, result_ad = detection(path_to_frozen_model='frozen_model/frozen_inference_graph.pb',
                            path_to_labels='frozen_model/label_map.pbtxt',
                            path_to_images='static/images/test.jpg',
                            path_to_results='static/images/' + generate_unique_id.generate_unique_id(),
                            min_score_thresh= min_threshold)
    data = analysis(output_dict, 5)
    data['address'] = result_ad
    data = json.dumps(data, cls= encoder)
    data = json.loads(data)

    return render_template('index.html', data = data)

@app.route('/')
def main():
    data = {'number': [],
            'max_score': [],
            'address': []}
    return render_template('index.html', data = data)

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html')

if __name__ == '__main__':
    app.run(debug= True)
