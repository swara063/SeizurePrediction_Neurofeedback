import tensorflow as tf
from tensorflow.keras.utils import register_keras_serializable

@register_keras_serializable()
def output_zeros(x):
    return tf.zeros((tf.shape(x)[0], 1))
