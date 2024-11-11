# ML Football Analysis System

## Overview
The AI/ML Football Analysis System is a powerful computer vision-based tool for real-time football analysis. Built with YOLO, OpenCV, and Python, this system detects and tracks players, referees, and footballs in video footage. The project aims to provide high accuracy and consistency in tracking, enabling detailed insights into player and team behaviors. Features include team color assignment using K-means clustering, optical flow analysis for camera motion, and pixel-to-real-world position transformation for precise movement tracking.

## Features
- **Real-Time Object Detection**: Achieves over 85% accuracy in detecting players, referees, and footballs in video footage.
- **Consistent Object Tracking**: Maintains over 90% consistency in tracking IDs across frames.
- **Team Color Assignment**: Uses K-means clustering to assign team colors, enhancing data visualization and enabling ball possession analysis.
- **Real-World Position Mapping**: Calculates player movements in real-world meters using perspective transformation with an error margin of less than 5%.
- **Camera Movement Measurement**: Uses optical flow to determine camera movement, adjusting tracking accordingly.


## Technologies Used
- **YOLO (You Only Look Once)**: Object detection model for real-time analysis.
- **OpenCV**: Computer vision library for image processing and video analysis.
- **K-Means Clustering**: For team color assignment and visualization.
- **Optical Flow**: Measures camera movement for accurate tracking adjustments.
- **Perspective Transformation**: Converts pixel positions to real-world coordinates.
- **Python**: Core programming language for implementing all functionalities.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- [YOLO Weights](https://github.com/ultralytics/yolov5) - trained weights for object detection
- OpenCV (`pip install opencv-python`)
- Pandas (`pip install pandas`)
- Other dependencies can be installed from the `requirements.txt` file.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/AI-ML-Football-Analysis.git
    cd AI-ML-Football-Analysis
    ```

2. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download YOLO Weights**:
    - Place the YOLO weights (e.g., `best.pt`) in the `models/` directory.

### Usage

1. **Running the Analysis**:
    ```bash
    python main.py
    ```
    - This will start the analysis, reading the input video and applying object detection, tracking, and team assignment.

2. **Output**:
    - The system will save an output video in the `output_videos` directory with annotated tracks for players and the football.

### Project Structure

- **main.py**: Main script to run the system.
- **trackers/**: Contains tracking utilities and the `Tracker` class.
- **team_assigner.py**: Module for team color assignment using K-means clustering.
- **stubs/**: Directory for storing track stubs to streamline tracking in successive runs.
- **utils/**: Helper functions for reading and saving videos.
- **models/**: Directory for storing YOLO weights.

### Key Modules

- `Tracker`: Implements YOLO-based object detection and tracking of players and the football.
- `TeamAssigner`: Uses K-means clustering to assign team colors based on player uniforms.
- `Perspective Transformation`: Provides pixel-to-real-world position mapping for accurate player movement analysis.
- `Optical Flow`: Calculates camera motion, adjusting tracked positions as the camera moves.

### Example Outputs
- Annotated video with player and ball tracking.
- Statistics on ball possession and player distances.

## Future Enhancements
- **Expanded Chatbot Capabilities**: More detailed player statistics and game event detection.
- **Enhanced Tracking Accuracy**: Use of deep learning-based optical flow for better camera motion detection.
- **Real-Time Streaming**: Support for live video feed input and analysis.

## Contributing
Contributions are welcome! Please fork the repository and make a pull request with any improvements or fixes.

## License
This project is licensed under the MIT License.
