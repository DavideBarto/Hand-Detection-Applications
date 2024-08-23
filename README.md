
# Hand Detection Applications

This project explores various applications based on hand detection using computer vision. It leverages the power of OpenCV and Mediapipe libraries to create interactive interfaces, including a finger painter, a rock-paper-scissors game, and a mouse controller.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Libraries Used](#libraries-used)
- [Future Work](#future-work)
- [References](#references)

## Introduction

The goal of this project is to explore different applications based on hand detection, enabling users to interact with computers through gestures. The applications developed include a finger painter, a rock-paper-scissors game, and a mouse controller. Each of these applications demonstrates the potential of computer vision to interpret and respond to hand movements.

## Features

- **Finger Painter**: Draw on the screen using hand gestures to select colors and brush sizes.
- **Rock-Paper-Scissors Game**: Play the classic game using hand gestures detected by the camera.
- **Mouse Controller**: Control the mouse pointer and perform clicks using hand gestures.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip package manager

### Step-by-Step Guide

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DavideBarto/Hand-Detection-Applications.git
   cd Hand-Detection-Applications
   ```

2. **Create a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Start the desired application by running the corresponding Python script:

   ```bash
   python finger_painter.py
   python rock_paper_scissors.py
   python mouse_controller.py
   ```

## Usage

### Finger Painter

- **Selection Mode**: Raise two fingers to enter selection mode and choose colors or brush sizes.
- **Drawing Mode**: Raise one finger to draw on the screen.
- **Eraser Tool**: Use a specific finger combination to erase drawings.

### Rock-Paper-Scissors Game

- Press `s` to start the game.
- The game will count down, and you can show your move using hand gestures.
- The application compares your move with the computer's random choice and displays the result.

### Mouse Controller

- Raise your index and middle fingers to move the mouse pointer.
- Perform a left click by bringing your thumb and index finger close together.
- Raise your ring finger to perform a right click.
- Control the volume by raising all fingers and moving your hand up or down.

## Project Structure

```
Hand-Detection-Applications/
│
├── finger_painter.py        # Script for the finger painter application
├── rock_paper_scissors.py   # Script for the rock-paper-scissors game
├── mouse_controller.py      # Script for the mouse controller application
├── requirements.txt         # Python dependencies
└── resources/               # Images and other resources for the interface
    └── ...
```

## Libraries Used

- **OpenCV**: For capturing video frames and handling image processing tasks.
- **Mediapipe**: For real-time hand tracking and gesture detection.
- **PyAutoGUI**: For controlling the mouse and keyboard programmatically.
- **PyCaw**: For controlling the system audio in the mouse controller application.

## Future Work

- Adding more interactive games like Tic-Tac-Toe.
- Enhancing the mouse controller with gestures for drag-and-drop, zooming, and scrolling.
- Implementing dual-hand drawing in the painter application.
- Integrating the hand detection module with a robotic arm for gesture-based control.

## References

- [OpenCV](https://opencv.org/)
- [Mediapipe](https://mediapipe.dev/)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)
- [PyCaw Library](https://github.com/AndreMiras/pycaw)
- [Creating a Virtual Painting App](https://analyticsindiamag.com/how-to-create-a-virtual-painting-app-using-opencv/)
- [Hand Gesture Recognition with Python and OpenCV](https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c)
- [Building a Hand Tracking System](https://www.analyticsvidhya.com/blog/2021/07/building-a-hand-tracking-system-using-opencv/)
