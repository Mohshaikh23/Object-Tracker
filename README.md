# Object Tracking Application

This is a simple object tracking application using OpenCV.

## Description

The application allows you to track an object in real-time using your webcam. It utilizes the CSRT tracker algorithm provided by OpenCV. The tracked object is visualized by drawing a bounding box around it in each frame.

https://github.com/Mohshaikh23/Object-Tracker/assets/93477768/d5a3d791-0718-40d5-8a8c-ba61f0ff40e3

## Features

- Real-time object tracking using OpenCV
- Bounding box visualization for the tracked object
- Video recording of the tracked object

## Installation

1. Clone the repository to your local machine.
   git clone <https://github.com/Mohshaikh23/Object-Tracker.git>
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the `tracker.py` script to start the application.

## Usage

1. Launch the application by running the `app.py` script.
2. A window named "Tracking" will open, displaying the webcam feed.
3. Select the object to be tracked by drawing a bounding box around it using the mouse. Press Enter to confirm the selection.
4. The application will start tracking the object and draw a bounding box around it in each frame.
5. The tracked video will be recorded and saved as "Application check.avi" in the current directory.
6. Press 'q' to exit the application.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

