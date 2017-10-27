import sys
sys.path.append('/root/miniconda3/lib/python3.4/site-packages')

from keras.models import model_from_json
from keras.models import load_model
import cv2
import imutils

from preprocess_dataset import preprocess_image

class NeuralNetworkPredictor:

    def predict_angle(self, image):
        image = preprocess_image(image)
        result = float(self.model.predict(image.reshape(1, 64, 64, 1), batch_size=1))
        # interpolated = 1470 + result * 490
        return int(result)

    def initialize(self):
        print('loading model')
        with open('out.json', encoding='utf-8') as net:
            model_text = net.read()
            self.model = model_from_json(model_text)
        print('model loaded, loading weights')
        self.model.load_weights('out.h5')
        print('weights loaded')
        print('d')
