import tensorflow as tf
from tensorflow.keras.models import load_model
from utils.config import cfg

# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

weather_model = load_model(cfg.path_model)