import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# 1. Load dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize pixel values (0–255 -> 0–1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2. Build model
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),     # Input layer
    layers.Dense(128, activation='relu'),     # Hidden layer
    layers.Dense(10, activation='softmax')    # Output layer
])

# 3. Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train model
model.fit(x_train, y_train, epochs=5)

# 5. Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)

# 6. Make predictions
predictions = model.predict(x_test)

# Show first image and predicted label
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Prediction: {predictions[0].argmax()}")
plt.show()
