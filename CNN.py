import tensorflow as tf
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

# Đường dẫn đến thư mục chứa dữ liệu
TRAINING_DIR = "C:\\Users\\Thanh Lam\\Desktop\Dataset-RPS\\train"
training_datagen = ImageDataGenerator(rescale = 1./255)

VALIDATION_DIR = "C:\\Users\\Thanh Lam\\Desktop\\Dataset-RPS\\val"
validation_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = training_datagen.flow_from_directory(
    TRAINING_DIR,
    target_size=(150,150),
    class_mode='categorical',
    batch_size=126
)

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(150,150),
    class_mode='categorical',
    batch_size=126
)

# Model train
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop')

history = model.fit(train_generator,
                     epochs=25,
                     steps_per_epoch=20,
                     validation_data = validation_generator,
                     verbose = 1,
                     validation_steps=3)

model.save("train_3.h5"),
