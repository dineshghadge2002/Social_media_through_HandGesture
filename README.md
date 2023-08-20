
# Gesture-Controlled Social Media Profile Opener

This Python script uses hand gestures to control the opening of various social media profiles. It utilizes the OpenCV library and the `cvzone` HandTrackingModule to detect hand gestures from a webcam feed and trigger actions based on those gestures.

## Features

- Open your LinkedIn, Kaggle, GitHub, Facebook, Instagram, and Snapchat profiles using hand gestures.
- Intuitive hand gestures are mapped to specific social media profiles.

## Prerequisites

- Python 3.x
- `opencv-python` library
- `cvzone` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dineshghadge2002/Social_media_through_HandGesture.git
   
   cd HandGestureSocialMediaOpener
   ```

2. Install the required libraries:

   ```bash
   pip install opencv-python
   pip install cvzone
   ```

## Usage

1. Run the script:

   ```bash
   python gesture_controlled_social_media_opener.py
   ```

2. A webcam feed will open, and you'll see the options to open different social media profiles based on hand gestures.

3. Perform the specified hand gestures to open the corresponding social media profiles.

4. Press the `Enter` key to exit the script.

## Gesture Mapping

- Thumb Up: Open LinkedIn profile
- Index Finger Up: Open Kaggle profile
- Middle Finger Up: Open GitHub profile
- Ring Finger Up: Open Facebook profile
- Little Finger Up: Open Instagram profile
- All Fingers Up: Open Snapchat profile

## Note

- The script uses the `os.system` command to open URLs, which might not work on all systems or may have security implications. Ensure the script is run in a controlled environment.
- Make sure your webcam is accessible by the script.

## Disclaimer

This script is provided as-is and may have limitations and security considerations. Use it responsibly and consider security implications when opening URLs using the `os.system` command.
# Social_media_through_HandGesture
