## Handwritten Digits Recognition

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdarshZolekar/Handwritten-Digits-Recognition/blob/main/MNIST-Digits-Recognition.ipynb)

A simple deep learning project using TensorFlow and Keras to classify handwritten digits (0–9) from the MNIST dataset. This project demonstrates how to build, train, and evaluate a basic neural network for image classification.

## Model Architecture

- **Input Layer:** 28x28 pixels (flattened to 784)
- **Hidden Layer:** Dense(128, ReLU)
- **Output Layer:** Dense(10, Softmax)

---

## Dataset

- Training images: 60,000  
- Test images: 10,000  
- Image size: 28x28 (grayscale)

---

## How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/AdarshZolekar/Handwritten-Digits-Recognition.git
   cd Handwritten-Digits-Recognition
   ```
2. Install dependencies:
   ```
   pip install -r Requirements.txt
   ```

3. Run the project:
   ```
   python MNIST-Digits-Recognition.py
   ```

---

## Requirements

- Python 3.x

- TensorFlow

- NumPy

- Matplotlib

Install them with:

```
pip install tensorflow numpy matplotlib
```

---

## Learning Outcome

- Basics of neural networks

- Hands-on with TensorFlow & Keras

- Experience in image preprocessing

---

## Future Improvements

- Switch from a simple dense network to a Convolutional Neural Network (CNN) for higher accuracy 
 
- Add a Streamlit/Gradio app for interactive digit drawing and real-time predictions  

- Deploy model on web/mobile using TensorFlow Lite or Flask API  

- Experiment with additional datasets (letters, symbols) for broader recognition 
 
- Hyperparameter tuning and regularization to reduce overfitting  

---

## License

This project is open-source and free to use for educational purposes.

---

## Contributions

Feel free to open issues or submit pull requests for improvements or bug fixes!

<p align="center">
  <a href="#top">
    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>
  </a>
</p>
