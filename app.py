from flask import Flask, render_template, request
import picamera
import time
import os

app = Flask(__name__)

def capture_image():
    camera = picamera.PiCamera()
    time.sleep(1)
    img_path = os.path.expanduser('~/flask_app/static/image.jpg')
    camera.capture(img_path)
    camera.close()

@app.route('/')
def hello_world():
    return "what's up"
    
@app.route('/static_image', methods = ['POST', 'GET'])
def static_image():
    if request.method == 'POST':
        if request.form['snapshot']:
            capture_image()
    return render_template('static_image.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1983, debug=True)
