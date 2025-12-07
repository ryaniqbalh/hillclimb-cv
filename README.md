# 🖐️ Hill Climb Racing (Python + Computer Vision)

This project is a fun computer vision experiment where I control the game **Hill Climb Racing** using only my hand gestures no keyboard input required.

By using *MediaPipe Hands* to detect whether my hand is open or closed, the system triggers **Gas** and **Brake** actions in real time through simulated keyboard inputs.  
This creates a simple but intuitive gesture-based gameplay experience.

---

## 🎮 Project Overview

In this experiment:

- **Right hand open → Gas**
- **Left hand open → Brake**
- Both hands open simultaneously → both actions triggered  
- Gestures are detected using **MediaPipe**, and commands are sent to the game using **PyAutoGUI**

This project demonstrates how computer vision can be used for **real-time interaction**, bridging physical gestures with digital control.

---

## 🧠 Technologies Used

- **Python 3**
- **OpenCV** — webcam stream & image processing  
- **MediaPipe Hands** — hand landmark detection & gesture logic  
- **PyAutoGUI** — simulate keyboard inputs to the game  
- **NumPy** — calculations & processing support  

---

## 🛠️ How It Works

1. Webcam captures real-time video frames  
2. MediaPipe detects 21 hand landmarks  
3. The script checks whether fingers are **extended or folded**  
4. Based on gesture state, it triggers:
   - `right` key for Gas  
   - `left` key for Brake  
5. Keyboard events are sent instantly to Hill Climb Racing  
6. The result is a natural, hands-free game controller

---

## 📷 Demo

*(Insert GIF or screenshot here if you want — optional)*

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/ryaniqbalh/HillClimbRacing-HandControl
cd HillClimbRacing-HandControl
