# GPT-3.5 Chat Assistant with Flask

This is a simple Flask web application that utilizes OpenAI's GPT-3.5 model to create a chat assistant. Users can interact with the chat assistant by entering text prompts, and the assistant will respond based on the input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3
- Flask
- OpenAI Python package

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/irohanrajput/pybot.git
```

2. Navigate into the project directory:

```
cd pybot
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

### Usage

1. Obtain an API key from OpenAI and save it in a file named `apikey.json` in the root directory of the project where your 'main.py' file exists. The format should be:

```json
{"key": "YOUR_API_KEY_HERE"}
```

2. Run the Flask application:

```
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000` to access the chat interface.

4. Enter text prompts in the input field and press Enter or click on the submit button to interact with the chat assistant.

## Acknowledgments

- This project utilizes OpenAI's GPT-3.5 model for natural language processing.
- The Flask web framework is used to create the web interface.
