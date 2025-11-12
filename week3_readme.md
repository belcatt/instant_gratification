# Week 3 — Convolutional Neural Networks (CNNs)

*Summary of Week 3 syllabus, Malaria project overview, and discussion highlights for INFS 6359: Data Mining for Business Analytics.*

---

## 📘 Course Context
This course introduces Unsupervised Learning and Deep Learning methods including CNNs, RNNs, GANs, and NLP. Students learn to use frameworks such as TensorFlow, PyTorch, and Google Colab for developing models in image recognition, text analysis, and reinforcement learning.

## 🎯 Week 3 Overview
Focus: **Convolutional Neural Networks (CNNs)** for image classification and pattern recognition.  
Students design, build, and evaluate CNNs like **AlexNet**, **VGG**, and **ResNet** with metrics such as accuracy and AUC.

### Learning Objectives
- Formulate computer vision problems using CNNs  
- Gather and preprocess image data  
- Train CNNs with TensorFlow, PyTorch, and Keras  
- Evaluate models using loss and accuracy metrics  

## 🧫 Malaria Cell Classification Project
Students applied CNNs to classify cell images as *Parasitized* or *Uninfected* using the Kaggle dataset “Cell Images for Detecting Malaria.”  
Transfer learning with VGG16 and ResNet50 was used in Google Colab with GPU acceleration.

**Dataset:** ~27k images (infected & healthy cells)  
**Models:** VGG16, ResNet50, AlexNet  
**Tools:** TensorFlow, Keras, Colab (GPU)  
**Metrics:** Accuracy, AUC, ROC Curve, Confusion Matrix  

_Key finding:_ ResNet50 achieved higher generalization due to skip connections, while VGG16 required more training time.

## 💬 Discussion Highlights
- Importance of balanced datasets for medical imaging  
- Dropout and early stopping reduce overfitting  
- GPU acceleration improves training time and model complexity  
- Transfer learning shortens training and improves results  

## 📚 References
- [GeeksforGeeks – Introduction to CNNs](https://www.geeksforgeeks.org/introduction-convolution-neural-network/)
- [Goodfellow et al. (2017) – Deep Learning Book](https://deeplearningbook.org)
- [VGG Architecture Overview](https://builtin.com/machine-learning/vgg16)
- [AlexNet Architecture – YouTube](https://www.youtube.com/watch?v=c_u4AHNjOpk)

