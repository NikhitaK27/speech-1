
# DRDO-DYSL Speech Recognition

DRDO-DYSL Speech Recognition is a comprehensive Python project for transcribing audio content accurately. It focuses on utilizing advanced models like Wav2Vec2 for converting spoken language into written text and is designed for ease of use and high accuracy in diverse environments.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [How to Use](#how-to-use)
- [Tools and Technologies](#tools-and-technologies)
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

1. **Open the Notebook in Colab**:
   - Navigate to the GitHub repository where the notebook [TASK_1_DRDO.ipynb](https://colab.research.google.com/drive/1u88709G27sinBHp8ysvv_0YyGIo8wr5m?usp=sharing) is hosted.
   - Open the notebook file and click on the "Open in Colab" button usually available at the top of the file in GitHub.

2. **Run the Notebook**:
   - Once in Google Colab, you can run the notebook cell by cell or run all cells at once using the runtime options.

3. **Install Dependencies**:
   - Before executing the cells, ensure that all dependencies are installed by running the following cell at the beginning of the notebook:
     ```bash
     !pip install torch torchaudio librosa transformers jiwer
     ```

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
