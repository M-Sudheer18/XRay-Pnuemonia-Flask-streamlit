# 🩻 AI Chest X-Ray Pneumonia Detection

## Problem Statement

Pneumonia is one of the leading causes of respiratory illness worldwide, and timely diagnosis is essential for effective treatment. Manual analysis of chest X-ray images requires experienced radiologists and can be time-consuming, especially in healthcare environments with high patient volumes.

**AI Chest X-Ray Pneumonia Detection** addresses this challenge by providing an AI-powered web application that automatically analyzes chest X-ray images and predicts whether the patient is **NORMAL** or has **PNEUMONIA**. By leveraging Deep Learning and a scalable cloud-based architecture, the system delivers fast, accurate, and user-friendly predictions to assist healthcare professionals, students, and researchers.

---

# 🌍 Context

Recent advancements in **Artificial Intelligence**, **Deep Learning**, and **Computer Vision** have significantly improved automated medical image analysis. Convolutional Neural Networks (CNNs) and Transfer Learning models such as **VGG16** have demonstrated high performance in detecting diseases from medical imaging.

This project combines multiple modern technologies to build a complete AI application:

- 🧠 TensorFlow & Keras for Deep Learning
- ⚙️ Flask REST API for backend inference
- 🌐 Streamlit for an interactive frontend
- 🤗 Hugging Face Hub for model hosting
- ☁️ Render for cloud deployment
- 🚀 Streamlit Community Cloud for frontend hosting

The application follows a production-inspired client-server architecture, where the frontend communicates with dedicated backend APIs for model inference, ensuring scalability and efficient resource utilization.

---

# 🎯 Objectives

The primary objectives of this project are:

## 🩺 Automated Pneumonia Detection

Develop a Deep Learning system capable of accurately classifying chest X-ray images into:

- 🟢 NORMAL
- 🔴 PNEUMONIA

using multiple trained AI models.

---

## 🤖 Multi-Model Prediction

Allow users to compare predictions using three Deep Learning models:

- CNN (10 Epochs)
- CNN (20 Epochs)
- VGG16 Transfer Learning

to evaluate different architectures and prediction performance.

---

## 🌐 Full Stack AI Deployment

Demonstrate how an AI model can be transformed into a real-world application by integrating:

- Streamlit Frontend
- Flask REST APIs
- Hugging Face Model Hosting
- Render Cloud Deployment

---

## ⚡ Real-Time Inference

Provide instant predictions with:

- Confidence Score
- Class Probabilities
- Selected Model Information

through an intuitive web interface.

---

# ⚙️ How It Works

## Step 1 — Image Upload

Users upload a Chest X-Ray image in one of the supported formats:

- JPG
- JPEG
- PNG

through the Streamlit web application.

---

## Step 2 — Model Selection

Users choose one of the available Deep Learning models:

- CNN (10 Epochs)
- CNN (20 Epochs)
- VGG16 Transfer Learning

The Streamlit frontend automatically routes the prediction request to the appropriate Flask backend service.

---

## Step 3 — Image Preprocessing

The backend validates and preprocesses the uploaded image according to the selected model.

### CNN Models

- Convert image to Grayscale
- Resize to 100 × 100
- Normalize pixel values
- Expand dimensions

### VGG16

- Convert image to RGB
- Resize to 100 × 100
- Apply `preprocess_input()`
- Expand dimensions

---

## Step 4 — Deep Learning Prediction

The selected TensorFlow model performs inference on the processed image.

The backend generates:

- Prediction Label
- Confidence Score
- Class Probability Distribution

---

## Step 5 — Result Visualization

The Flask backend returns a JSON response to the Streamlit frontend, which displays:

- 🩺 Predicted Class
- 📊 Confidence Score
- 📈 Probability Distribution
- 🤖 Selected Deep Learning Model

---

# 🏗️ System Architecture

```text
                          👤 User
                             │
                             ▼
                 🌐 Streamlit Frontend (UI)
                             │
              Upload Image & Select AI Model
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
      ⚙️ Flask Backend (CNN)        ⚙️ Flask Backend (VGG16)
         Render Service #1             Render Service #2
              │                             │
              └──────────────┬──────────────┘
                             ▼
                  🤗 Hugging Face Model Hub
                             │
                 Automatic Model Download
                             │
                             ▼
                 🧠 TensorFlow Model Inference
                             │
                             ▼
                  JSON Prediction Response
                             │
                             ▼
                Streamlit Displays Prediction
```

---

# 🧠 Deep Learning Models

The application integrates three Deep Learning models to provide flexible and accurate predictions.

| Model | Architecture | Purpose |
|--------|--------------|---------|
| CNN (10 Epochs) | Custom CNN | Baseline Chest X-Ray Classification |
| CNN (20 Epochs) | Improved CNN | Enhanced Feature Extraction |
| VGG16 Transfer Learning | Pretrained CNN | High-Accuracy Medical Image Classification |

Each model predicts one of the following classes:

- 🟢 NORMAL
- 🔴 PNEUMONIA

---

# ☁️ Cloud Deployment

To ensure efficient deployment and overcome cloud memory limitations, the application is distributed across multiple cloud services.

## 🌐 Streamlit Community Cloud

Hosts the interactive web application.

### Live Demo

👉 https://pnuemonia-detection-cnn-vgg.streamlit.app/

---

## ⚙️ Flask Backend (CNN Models)

Handles predictions for:

- CNN (10 Epochs)
- CNN (20 Epochs)

### API Endpoint

👉 https://xray-pnuemonia-flask-streamlit-1.onrender.com

---

## ⚙️ Flask Backend (VGG16)

Handles predictions for:

- VGG16 Transfer Learning

### API Endpoint

👉 https://xray-pnuemonia-flask-streamlit-2.onrender.com

---

## 🤗 Hugging Face Hub

All trained Deep Learning models are hosted on Hugging Face Hub.

The backend automatically downloads and caches the required model during runtime, keeping the GitHub repository lightweight while ensuring faster deployments and easier model management.

---

# 🚀 Key Features

- 🩻 Chest X-Ray Image Classification
- 🤖 Multiple Deep Learning Models
- ⚙️ Flask REST API Backend
- 🌐 Interactive Streamlit Frontend
- ☁️ Hugging Face Model Hosting
- 🚀 Render Cloud Deployment
- 📊 Confidence Score
- 📈 Probability Distribution
- ⚡ Real-Time AI Prediction
- 🧹 Automatic Image Validation & Cleanup
- 🔄 Intelligent Backend Routing
- 📱 Responsive & User-Friendly Interface

---

# 📈 Project Outcome

**AI Chest X-Ray Pneumonia Detection** demonstrates how Deep Learning models can be successfully deployed as a **production-ready Full Stack AI application** using modern cloud technologies.

The project integrates **Computer Vision**, **Deep Learning**, **REST APIs**, and **Cloud Deployment** into a unified system that provides fast, accurate, and scalable medical image analysis.

By separating the frontend and backend services, hosting models on Hugging Face, and deploying dedicated Flask APIs on Render, the application showcases a scalable architecture suitable for real-world AI deployment.

This project highlights practical implementation of:

- Artificial Intelligence
- Computer Vision
- Deep Learning
- TensorFlow & Keras
- Flask REST APIs
- Streamlit Development
- Hugging Face Integration
- Render Deployment
- Cloud-Based AI Applications
- Full Stack AI Engineering

making it a strong portfolio project for roles in **Machine Learning**, **AI Engineering**, **Computer Vision**, and **Full Stack AI Development**.

---

# 🌐 Live Project Links

## 🖥️ Streamlit Frontend

https://pnuemonia-detection-cnn-vgg.streamlit.app/

---

## ⚙️ Flask Backend (CNN Models)

https://xray-pnuemonia-flask-streamlit-1.onrender.com

---

## ⚙️ Flask Backend (VGG16)

https://xray-pnuemonia-flask-streamlit-2.onrender.com

---

## 🤗 Hugging Face Model Repository

https://huggingface.co/Sudheer17

---

## 💻 GitHub Repository

https://github.com/M-Sudheer18/XRay-Pnuemonia-Flask-streamlit
