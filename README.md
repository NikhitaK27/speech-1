wh
# DRDO-DYSL Speech Recognition

DRDO-DYSL Speech Recognition is a comprehensive Python project for transcribing audio content accurately. It focuses on utilizing advanced models like Wav2Vec2 for converting spoken language into written text and is designed for ease of use and high accuracy in diverse environments.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Dataset](#dataset)
- [Tools and Technologies](#tools-and-technologies)
- [Results](#results)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Speech-to-Text Conversion**: Implements state-of-the-art speech recognition using Wav2Vec2 to transcribe audio files.
- **LibriSpeech Dataset**: Uses a diverse dataset for training and testing, ensuring robust model performance.
- **Offline Functionality**: Can be run locally, ensuring data privacy and security.
- **Ease of Setup**: Designed for quick setup with detailed instructions, allowing users to start transcribing quickly.

## Prerequisites

- Python 3.x
- torchaudio
- librosa
- transformers
- jiwer

## Setup and Installation

### Clone the Repository

```bash
git clone https://github.com/vikramkumar402/DRDO-DYSL-Speech-Recognition.git
cd DRDO-DYSL-Speech-Recognition
```

### Installation

Before running the scripts or notebooks, install the required Python packages using the following commands:

```bash
pip install torch
pip install torchaudio
pip install librosa
pip install transformers
pip install jiwer
```

## Running the Project

You can run this project using Google Colab, which allows you to execute the notebook in a cloud environment without needing to install the dependencies locally.

### Running on Google Colab

Click the button below to open the Jupyter notebook in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vikramkumar402/DRDO-DYSL-Speech-Recognition)

### Local Setup

If you prefer to run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-github-username/DRDO-DYSL-Speech-Recognition.git
   cd DRDO-DYSL-Speech-Recognition
   ```

2. **Install Dependencies**:
   ```bash
   pip install torch
   pip install torchaudio
   pip install librosa
   pip install transformers
   pip install jiwer
   ```

3. **Run the Script**:
   ```bash
   python task_1_drdo.py
   ```
## Dataset

This project leverages the *LibriSpeech Dataset*, an extensive collection of approximately 1000 hours of English speech recorded at a 16kHz sampling rate. Originating from read audiobooks in the LibriVox project, this dataset is well-recognized in the research community for speech recognition tasks.

### Dataset Details:

- *Source*: Derived from audiobooks available on LibriVox.
- *Audio Quality*: All audio files are at 16kHz, which is suitable for voice recognition systems.
- *Variety*: The dataset includes multiple subsets categorized by the cleanliness of the recordings and the diversity of accents and speaking styles. For this project, the following subsets are used:
  - *Train-Clean-100*: 100 hours of clean training data, ideal for initial model training.
  - *Train-Clean-360*: 360 hours of clean training data, used for more extensive training to improve model robustness.
  - *Test-Clean*: Clean test data used for final model evaluation.
  - *Test-Other*: More challenging test data that includes a variety of accents and more complex audio scenarios.

### Usage in the Project:

The LibriSpeech dataset was integral to developing and testing the speech recognition model. Using different subsets allowed for a thorough evaluation of the model's accuracy across varying audio conditions:
- *Training Phase*: Utilized 'Train-Clean-100' and 'Train-Clean-360' for training the model, focusing on understanding and accurately transcribing clean speech.
- *Testing Phase*: Tested the model using 'Test-Clean' to assess performance under ideal conditions and 'Test-Other' to evaluate robustness in handling diverse and challenging audio scenarios.

This structured use of the dataset helps in pinpointing the strengths and limitations of the speech recognition model, providing clear pathways for further enhancements.
## Tools and Technologies

<table>
  <tr>
    <th>Area</th>
    <th>Tool/Technology</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Speech Recognition</td>
    <td>Wav2Vec2</td>
    <td>Used for accurate speech-to-text conversion.</td>
  </tr>
  <tr>
    <td>Audio Processing</td>
    <td>torchaudio, librosa</td>
    <td>Handle audio file processing and manipulation.</td>
  </tr>
  <tr>
    <td>Programming Language</td>
    <td>Python</td>
    <td>The core language used for developing the application.</td>
  </tr>
</table>


## Results

The performance of the speech recognition model was evaluated using the Character Error Rate (CER), which is a common metric in speech and handwriting recognition that measures the minimal number of character insertions, deletions, and substitutions required to change the recognized text into the reference text.

Here are the results tabulated:

| Dataset          | Average CER  |
|------------------|--------------|
| Train-Clean-100  | 0.002039     |
| Train-Clean-360  | 0.001401     |
| Test-Clean       | 0.008527     |
| Test-Other       | 0.011143     |

These results indicate a high level of accuracy in the transcription of audio from the LibriSpeech dataset, especially in cleaner audio conditions.

## Conclusion

The low CER values demonstrate the effectiveness of the Wav2Vec2 model in transcribing audio accurately under diverse conditions. The model shows exceptional performance on cleaner datasets (train-clean-100 and train-clean-360) and maintains good accuracy even in more challenging datasets (test-clean and test-other).

This project highlights the potential of using advanced deep learning models for robust speech-to-text applications. Future improvements might include fine-tuning the model on specific accents or dialects to further enhance its accuracy and versatility in real-world applications.
## Contributing

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more similar items.

## Contact

Vikram Kumar - vikramk.ug22.cs@nitp.ac.in

LinkedIn: [linkedin.com/in/vikramkumar2510/](https://www.linkedin.com/in/vikramkumar2510/)

Project Link: [DRDO-DYSL Speech Recognition](https://github.com/vikramkumar402/DRDO-DYSL-Speech-Recognition)
