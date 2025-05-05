import tensorflow as tf
from tensorflow.keras.layers import Layer

class OutputZeros(Layer):
    def call(self, inputs):
        return tf.zeros_like(inputs)

def output_zeros(x):
    return tf.zeros_like(x)
