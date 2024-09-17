# Jewelry Chatbot Application

This is a demo chatbot application designed to handle jewelry-related queries. The application performs real-time interactions with users through Socket.IO and streams responses with Markdown-enhanced formatting.

![Screenshot 2024-09-17 143353](https://github.com/user-attachments/assets/205a1e30-cb8e-4ff4-911b-1fd00806a2b3)


## Features

- **Safety check**: All prompts are checked to ensure they are safe.
- **Jewelry-focused evaluation**: Only jewelry-related queries are processed.
- **Real-time interaction**: Responses are streamed to the client using Socket.IO.
- **Markdown formatting**: Responses are dynamically rendered with Markdown formatting for enhanced readability.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- Virtual environment (`venv`)
- Required packages (specified in `requirements.txt`)

You will also need your own AI keys to access the chatbot functionalities. These should be included in the `.env` file (explained below).

## Setup

### 1. Clone the repository

First, clone this repository to your local machine:

```
git clone https://github.com/Pipzzter/chatbot-app-demo.git
cd chatbot-app-demo
```

### 2. Setup the virtual environment
Before installing dependencies, you need to activate a virtual environment:

For Windows:
```
python -m venv venv
venv\Scripts\activate
```
For Linux:
```

python3 -m venv venv
source venv/bin/activate
```
For macOS:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
With the virtual environment activated, install the required packages:

```
pip install -r requirements.txt
```

### 4. Setup the .env file
Create a .env file in the root of the project with your AI keys. The file should include at least the following environment variables:

OPENAI_API_KEY=your_openai_key
HUGGINGFACE_API_KEY=your_huggingface_key
HUGGINGFACE_BASE_URL=your_huggingface_base_url

Replace your_openai_key, your_huggingface_key, and your_huggingface_base_url with your actual API keys.

### 5. Start the application
With everything set up, start the application from the root of the project using the following command:
```
python -m chatapp.main
```
This command will launch the application, allowing you to interact with the jewelry chatbot.

### 6. Access the Application
Once the application is running, you can access the chatbot by opening your browser and navigating to the locally hosted server (typically at http://localhost:5000).
