# mouse_tracing_with_eyes
Mouse Control Using Eye Movements 
# 👁️ Mouse Control Using Eye Movements

## 📌 Project Overview

This project is a computer vision-based system that enables users to control the mouse cursor using eye movements. It uses real-time webcam input to track eye position and translate it into cursor movement, allowing hands-free interaction with the computer.

---

## 🚀 Features

* Real-time eye tracking using webcam
* Cursor movement based on eye direction
* Blink detection for mouse clicks
* Hands-free system interaction
* Lightweight and efficient implementation

---

## 🛠️ Tech Stack

* Python
* OpenCV (`cv2`)
* Mediapipe / Dlib (for facial landmark detection)
* NumPy

---

## ⚙️ How It Works

The system captures live video using the webcam and processes each frame to detect facial landmarks. It focuses on the eyes to track movement and determines the direction of gaze. Based on this, the mouse cursor is moved on the screen. Eye blinks are detected and used to simulate mouse clicks.

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/mouse_tracing_with_eyes.git
```

### 2. Navigate to project folder

```
cd mouse_tracing_with_eyes
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the project

```
python main.py
```

---

## 📊 Applications

* Assistive technology for physically disabled users
* Hands-free computer control
* Human-computer interaction systems
* AI-based accessibility tools

---

## 🔮 Future Improvements

* Improve tracking accuracy and speed
* Add gesture-based controls
* Enhance UI/UX
* Support multi-monitor setups

---

## 🤝 Contribution

Feel free to fork this repository and contribute to improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---
