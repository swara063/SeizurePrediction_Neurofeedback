from tensorflow.keras.models import load_model
from models.custom_layers import output_zeros  # Import the custom function

def load_prediction_model():
    model = load_model("models/model.h5", custom_objects={"output_zeros": output_zeros})
    return model
