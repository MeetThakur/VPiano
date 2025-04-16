---

# 🎵 Hand Gesture Controlled Sound Player

This project uses **MediaPipe**, **OpenCV**, and **Pygame** to track hand gestures in real-time using a webcam. Each finger gesture (bending) plays a unique sound, making it an interactive way to explore hand tracking and sound feedback.

---

## 🧠 Features

- Real-time hand tracking using MediaPipe.
- Detection of individual finger bend angles.
- Plays different sounds based on finger gestures.
- Visual feedback via OpenCV window.
- Works with both hands.

---

## 📦 Requirements

Install the following Python packages before running the code:

```bash
pip install opencv-python mediapipe pygame numpy
```

---

## 📁 Folder Structure

```
.
├── main.py                # Main script
├── sounds/                # Folder containing sound files
│   ├── 1.mp3              # Sound for Thumb
│   ├── 2.mp3              # Sound for Index
│   ├── 3.mp3              # Sound for Middle
│   ├── 4.mp3              # Sound for Ring
│   └── 5.mp3              # Sound for Pinky
```

---

## 🚀 How to Run

1. Make sure your webcam is connected.
2. Place the required sound files inside a folder named `sounds/` in the root directory.
3. Run the script:

```bash
python main.py
```

4. Show your hand to the webcam. When you bend any finger, its corresponding sound will play.

5. Press **`q`** to quit the application.

---

## 🛠️ How It Works

- Uses MediaPipe to detect hand landmarks.
- Calculates angles between joints to determine finger bending.
- Triggers sound playback if finger is bent below a certain threshold.
- Provides on-screen visual feedback on the finger's status (Bent, Slightly Bent, Straight).

---

## 🧑‍💻 Author

**Meet Thakur**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
