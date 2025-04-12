from tensorflow.keras.models import load_model

def load_prediction_model(path='models/model.h5'):
    return load_model(path)
