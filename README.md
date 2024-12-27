# ECS Motion Detection Object Camera

## Overview
The `ECS-motion-detection-object-camera` project is designed to detect motion and identify objects using a camera. This project leverages the power of ECS (Entity Component System) architecture to efficiently manage and process data, enabling real-time motion detection and object recognition.

## Features
- **Real-time Motion Detection:** Detects any movement in the camera's field of view.
- **Object Recognition:** Identifies and classifies objects within the detected motion.
- **Efficient Data Processing:** Utilizes ECS architecture for optimal performance and scalability.

## Getting Started

### Prerequisites
- Python 3.x
- OpenCV
- NumPy
- TensorFlow (or any other object detection library)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/bedead/ECS-motion-detection-object-camera.git
    cd ECS-motion-detection-object-camera
    ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
1. Run the main script to start the motion detection and object recognition:
    ```sh
    python main.py
    ```
2. Adjust the configuration settings in `config.py` as needed.
