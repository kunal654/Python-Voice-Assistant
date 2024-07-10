
# Kunal - Python Voice Assistant

Kunal is a simple voice assistant program built in Python using the `speech_recognition` library for speech recognition and `pyttsx3` for text-to-speech conversion. It responds to voice commands to perform tasks such as opening websites, fetching the current time, and opening applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Supported Commands](#supported-commands)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Speech recognition to understand user commands.
- Text-to-speech to respond with synthesized speech.
- Opens specified websites (e.g., YouTube, Google, GitHub, LinkedIn) based on user commands.
- Retrieves and announces the current time.
- Launches applications like Chrome and Notepad.

## Installation

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/kunal654/kunal-voice-assistant.git
cd kunal-voice-assistant
```

### Install Dependencies

Ensure you have Python installed. Install the required libraries using pip:

```bash
pip install speech_recognition pyttsx3
```

## Usage

Run the Python script to initialize Kunal:

```bash
python kunal_voice_assistant.py
```

Follow the instructions given by Kunal to interact with the voice assistant using your microphone.

## Functionality

### Listening to Commands

Kunal listens for commands through your microphone. It adjusts for ambient noise before listening to ensure accurate speech recognition.

### Speaking Responses

Once a command is recognized, Kunal converts the response into synthesized speech using the `pyttsx3` library.

### Opening Websites and Applications

Kunal can open specified websites such as YouTube, Google, GitHub, and LinkedIn using the default web browser. It also supports opening applications like Chrome and Notepad.

### Getting Current Time

By asking for the time, Kunal retrieves and announces the current time.

## Supported Commands

- **Hello**: Greet Kunal, and it responds with a random greeting.
- **Time**: Fetches and announces the current time.
- **Open YouTube/Google/GitHub/LinkedIn**: Opens the respective website in the default web browser.
- **Open Chrome/Notepad**: Launches the specified application.
- **Exit/Quit/Stop/Wait**: Terminates the program and says goodbye.

## Dependencies

- `speech_recognition`: For recognizing speech input from the microphone.
- `pyttsx3`: For converting text responses into synthesized speech.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact me directly at [kunalgautam489@gmail.com](mailto:kunalgautam489@gmail.com).

