from flask import Flask, render_template, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    image_dir = 'static/images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, 'captured_image.png')
    with open(image_path, 'wb') as f:
        f.write(image_data)
    return jsonify({'message': 'Image saved successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
