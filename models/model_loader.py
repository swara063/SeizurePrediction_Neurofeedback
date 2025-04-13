from tensorflow.keras.models import load_model

def load_prediction_model(path='models/model.h5'):
    """
    Load the trained model from the specified path.
    """
    return load_model(path)
