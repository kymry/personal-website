import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.text import tokenizer_from_json
import re
import json


def preload_model():
        ''' Returns nothing. Creates two global variables.
            model: the Keras model to perform sentiment analysis.
            tokenizer: the Keras tokenizer to tokenize predictions.
        '''
        global tokenizer
        global keras_model
        with open('application/sentiment/model/tokenizer.json') as f:
                json_data = json.load(f)
                tokenizer = tokenizer_from_json(json_data)
        with open('application/sentiment/model/model.h5') as f:
                keras_model = tf.keras.models.load_model(f)


def preprocess_text(text):
        ''' Returns the input text cleaned. html, punctuation, numbers, characters and
            extra white spaces are removed.

        Parameters:
            text (String): The text to clean.
        '''
        # remove html markup
        text = re.sub('<[^>]*>', '', text)
        # remove punctuations and numbers
        text = re.sub('[^a-zA-Z]', ' ', text)
        # remove single characters
        text = re.sub(r"\s+[a-zA-Z]\s+", ' ', text)
        # remove multiple spaces
        text = re.sub(r'\s+', ' ', text)

        return text


def predict(review):
        ''' Returns the sentiment of the input text. 0:negative, 1: positive.

        Parameters:
            review (String): The review to perform sentiment analysis on.
        '''
        review = preprocess_text(review)
        review = tokenizer.texts_to_sequences([review])
        review = pad_sequences(review, padding='post', maxlen=300)
        sentiment = keras_model.predict_classes(review)
        return 'positive' if sentiment[0] == 1 else 'negative'


def get_sentiment(prediction, correct, incorrect):
        ''' Returns the correct sentiment of the review, based on user input

        Parameters:
            prediction (Bool): The review prediction from the Keras model
            correct (Bool): True if the prediction was correct (user input)
            incorrect (Bool): True if the prediction was incorrect (user input)
        '''
        if (prediction == 'positive' and incorrect) or (prediction == 'negative' and correct):
                return 0
        return 1

