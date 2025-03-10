# Whisper WebUI

## Overview

Whisper WebUI is a user-friendly web application designed to transcribe and translate audio files using the OpenAI Whisper API. This application enhances accessibility and usability by allowing users to upload audio files and receive transcriptions or translations in various formats, catering to a wide range of applications.

## Demo

- Transcription: ![transcription](https://github.com/Education-Victory/whisper-webui/blob/main/transcription.gif?raw=true)
- Translation: ![translation](https://github.com/Education-Victory/whisper-webui/blob/main/translate.gif?raw=true)
- Online Demo: [Whisper WebUI](https://whisper-webui.streamlit.app/)


## Features

- **Multi-format Support**: Upload audio files in various formats, including FLAC, M4A, MP3, MP4, MPEG, MPGA, OGA, OGG, WAV, and WEBM.
- **Language Specification**: Specify the input language to improve transcription accuracy.
- **Custom Prompts**: Provide an optional prompt to guide the transcription style.
- **Flexible Output Formats**: Choose from multiple output formats, including JSON, plain text, SRT, verbose JSON, and VTT.

## Getting Started

### Run Online

1. Visit the [Whisper WebUI](https://whisper-webui.streamlit.app/) page.
2. Provide your OpenAI API Key.
3. Choose the **"Create transcription"** or **"Create translation"** button based on your usecase.
3. Upload an audio file and specify the  optional prompt, and desired output format.
5. View or download the results.

### Run Locally

To run Whisper WebUI on your local machine, follow these steps:

1. Clone the Repository:

   `git clone git@github.com:Education-Victory/whisper-webui.git`
   `cd whisper-webui`
2. Install Required Packages:

    `pip install -r requirements.txt`
3. Get OpenAI API Key:
    Ensure you have your OpenAI API key ready.
4. Run the Streamlit Application:

    `streamlit run app.py`

### Using Docker

There are three ways to run the application using Docker:

#### Using Docker Compose (Recommended)

1. Create a `.env` file with your configuration:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your settings:
   ```
   OPENAI_API_KEY="your-api-key"
   CUSTOM_API_BASE="https://api.openai.com/v1"
   CUSTOM_MODEL="whisper-1"
   ```

3. Start the container:
   ```bash
   docker compose up -d
   ```

4. Access the application at `http://localhost:8501`

#### Using Docker Directly

1. Build the Docker image:
   ```bash
   docker build -t whisper-webui .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 \
     -e OPENAI_API_KEY="your-api-key" \
     -e CUSTOM_API_BASE="https://api.openai.com/v1" \
     -e CUSTOM_MODEL="whisper-1" \
     whisper-webui
   ```

3. Access the application at `http://localhost:8501`

#### Using Portainer Stack Repository

1. In Portainer, go to Stacks → Add Stack

2. Choose "Repository" as build method and enter:
   - Repository URL: `https://github.com/adriabama06/whisper-webui-custom-server.git`
   - Repository reference: `main`
   - Compose path: `compose.portainer.yml`

3. Set your environment variables:
    ```bash
    OPENAI_API_KEY=your-api-key
    CUSTOM_API_BASE=https://api.openai.com/v1
    CUSTOM_MODEL=whisper-1
    PORT=8501
    ```

4. Deploy the stack and access the application at `http://your-server:8501`


## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue.
