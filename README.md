# PyChat

PyChat is a trainable chatbot built using Python's ChatterBot library. It can be trained with custom data to respond to user inputs in a conversational manner.

## Table of Contents
- Introduction
- Installation
- Usage
- Training
- Customization

## Introduction
PyChat uses ChatterBot, a machine learning conversational dialog engine, to create a flexible and trainable chatbot.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/PyChat.git
    cd PyChat
    ```

2. **Create a virtual environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the chatbot:
```bash
python main.py

# Training

## Create a Training File
Create a training file (e.g., `training_data.yml`):

```yaml
categories:
- greetings
conversations:
- - Hello
  - Hi there!
- - How are you?
  - I'm good, thank you!
