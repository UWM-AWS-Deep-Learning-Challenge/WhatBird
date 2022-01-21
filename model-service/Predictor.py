import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd

class Predictor():
    WEIGHTS_1060_PATH = '../data/valid/ALBATROSS/1.jpg'
    CLASS_DICT = '../data/class_dict.csv'

    def __init__(self, modelPath: str = WEIGHTS_1060_PATH) -> None:
        assert os.path.exists(modelPath), 'thats not a path bro'
        absolute = os.path.abspath(modelPath)
        self.model = load_model(absolute)

        assert os.path.exists(self.CLASS_DICT), 'class dict is not a valid path'
        self.class_dict = pd.read_csv(self.CLASS_DICT)

    def predict(self, path: str) -> dict:
        assert os.path.exists(path), 'I can\'t find that bird bro'

        # pre-processing
        bird = image.load_img(path, target_size=(224, 224))
        bird = np.asarray(bird)
        bird = np.expand_dims(bird, axis=0)

        # make the prediction! the model returns a list of confidence values, one for each class
        prediction = self.model.predict(bird)
        prediction = prediction[0] # make the array 1d

        # get an array of sorted indeces
        prediction_sorted = np.argsort(prediction)

        # get the top three species
        topThreeBirds = []
        topThreeScores = []
        for i in range(3):
            birdName = self.class_dict['class'][prediction_sorted[i]]
            birdScore = prediction[prediction_sorted[i]]

            topThreeBirds.append(birdName)
            topThreeScores.append(birdScore)

        # map the results and return 
        prediction_map = {
           "results" : {
               "0" : {
                   "species" : str(topThreeBirds[0]),
                   "confidence": str(topThreeScores[0])
                },
               "1" : {
                   "species" : str(topThreeBirds[1]),
                   "confidence": str(topThreeScores[1])
                },
               "2" : {
                   "species" : str(topThreeBirds[2]),
                   "confidence": str(topThreeScores[2])
                },
           }
        }
        return prediction_map


