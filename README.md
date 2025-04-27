# Sign Language Segmentation & Classification Experiment

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yonathan-Ashebir/sign_language_classifer/blob/main/main.ipynb)

<div align="center">
  <!-- <img src="https://storage.googleapis.com/kaggle-datasets-images/3258/5339/4e4f183e7a5e0a8d7a1c4a8f8d0a8b8d/dataset-cover.jpg" width="400" alt="ASL Dataset Example"> -->
  <p>American Sign Language (ASL) Alphabet Dataset</p>
</div>

## Project Description

This project experiments with different approaches to segment and classify sign language images. The current implementation uses:

- **MediaPipe** for real-time hand segmentation and tracking
- **Custom CNN architecture** for classifying 26 ASL letters (A-Z)

## Key Features

- Real-time hand detection and segmentation
- 28x28 grayscale image processing
- CNN-based classification with 26 output classes
- Adjustable hand detection sensitivity
- Lateral inversion option for more natural interaction
- Jupyter notebook and OpenCV display options

## Architecture

The classification model uses this CNN architecture:

```python
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        
        # Convolutional layers + BatchNorm
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout2d = nn.Dropout2d(0.2)
        
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        self.pool2 = nn.MaxPool2d(2, 2)
        
        # Adaptive Global Average Pooling to (1,1)
        self.gap = nn.AdaptiveAvgPool2d((1, 1))
        
        # Fully connected layers
        self.fc1 = nn.Linear(128, 128)
        self.dropout = nn.Dropout(0.4)
        self.fc2 = nn.Linear(128, 26)  # 26 classes for A-Z
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Yonathan-Ashebir/sign_language_classifer.git
cd yourrepo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

For Jupyter notebook demo:
```bash
jupyter notebook main.ipynb
```

Toggle configurations like `USE_PRETRAINED`, `TEST_LIVE` to your needs.

## Configuration

Adjust these parameters in the code:

- `HAND_SELECTOR_SENSITIVITY`: Controls hand selection area (1.5-2.5 recommended)
- `LATERAL_INVERT`: Set to True for mirrored camera view
- `MIN_DETECTION_CONFIDENCE`: Hand detection sensitivity (0-1)
- `MIN_TRACKING_CONFIDENCE`: Hand tracking sensitivity (0-1)

<!-- ## Developers

- [Developer 1](https://github.com/dev1)
- [Developer 2](https://github.com/dev2)
- [Developer 3](https://github.com/dev3) -->
