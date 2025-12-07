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

## 🔧 Installation

**Make sure you already install Hill Climb Racing**  
   You can download the game directly from the **Microsoft Store** on Windows.
   
Follow the steps below to set up the Hand Gesture Controller for Hill Climb Racing:

1. Clone the repository
   ```bash
   git clone https://github.com/ryaniqbalh/HillClimbRacing-HandControl  
   cd HillClimbRacing-HandControl  

3. Create and activate a virtual environment
   ```bash
   python -m venv .env  
   .\.env\Scripts\activate   # Windows  

5. Install dependencies
   ```bash
   pip install -r requirements.txt  
   # Or install manually:  
   pip install opencv-python mediapipe pyautogui numpy  

7. Run the program
   Before running the script, make sure Hill Climb Racing is already open on your screen.
   The gesture controller works by sending keyboard inputs to the active game window.
   ```bash
   python hillclimb_hand_controller.py  

Make sure Hill Climb Racing is already open, then raise your hands and start playing!

