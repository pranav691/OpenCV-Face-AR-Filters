# 🎭 Advanced Real-Time AR Face Filter System

### Built with OpenCV + MediaPipe (FaceMesh)

A full-feature Augmented Reality (AR) filter system built in Python
using **OpenCV**, **MediaPipe FaceMesh**, and **PNG overlay
rendering**.\
It supports **hats, glasses, and moustache filters** with rotation,
smoothing, and real-time facial tracking---similar to Snapchat &
Instagram filters.

------------------------------------------------------------------------

## 🎥 Demo (GIF Placeholder)

*(Add your GIF here)*

------------------------------------------------------------------------

## 🚀 Features

### ✔ Real-Time Face Tracking

Uses **MediaPipe FaceMesh (468 landmarks)** for accurate forehead, chin,
cheek, and mid-face detection.

### ✔ PNG Transparency Support

Supports **alpha-channel overlays**, creating clean, professional filter
effects.

### ✔ Multiple AR Filters

Switch between: - Hats\
- Glasses\
- Moustache

### ✔ Face Rotation Support

Automatically rotates filters using cheek-landmark angle.

### ✔ Smoothing / No Shaking

Applies historical smoothing for stable overlays during head movement.

### ✔ Keyboard Controls

Switch modes & cycle filters instantly.

### ✔ Clean and Optimized Code

Minimal, well-structured, production-ready.

------------------------------------------------------------------------

## 🧠 Tech Stack

  Technology               Purpose
  ------------------------ --------------------------------
  **Python**               Core programming
  **OpenCV**               Image processing + webcam feed
  **MediaPipe FaceMesh**   Landmark tracking (468 points)
  **NumPy**                Math + array handling
  **PNG Transparency**     Alpha blending overlays

------------------------------------------------------------------------

## ⌨️ Controls

  Key       Action
  --------- --------------------------
  **1**     Switch to Hat mode
  **2**     Switch to Glasses mode
  **3**     Switch to Moustache mode
  **H**     Next hat
  **G**     Next glasses
  **M**     Next moustache
  **ESC**   Exit the program

------------------------------------------------------------------------

## 📁 Folder Structure

    Project/
    │
    ├── main.py
    ├── README.md
    │
    └── Resources/
        ├── hats/
        │   ├── hat1.png
        │   ├── hat2.png
        │   └── hat3.png
        │
        ├── glasses/
        │   ├── glasses1.png
        │   └── glasses2.png
        │
        └── moustache/
            └── moustache1.png

------------------------------------------------------------------------

## 🖼️ Sample Filters (Screenshots Placeholder)

(Add screenshots here)

------------------------------------------------------------------------

## 📦 Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2️⃣ Install Dependencies

``` bash
pip install opencv-python mediapipe numpy
```

### 3️⃣ Run the Program

``` bash
python main.py
```

------------------------------------------------------------------------

## 🧩 How It Works (Short Explanation)
