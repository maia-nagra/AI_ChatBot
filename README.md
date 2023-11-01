# Running the Chatbot

## Prerequisites
- Python 3.7.1 or a later version
- An Azure subscription
- Access granted to Azure OpenAI in the desired Azure subscription
- An Azure OpenAI Service resource with a gpt-35-turbo-instruct model deployed.

## To Run Locally
Create a .env on the top level folder with the following format:

OPENAI_API_KEY=xxxx

OPENAI_API_BASE=xxxx

OPENAI_API_TYPE=azure

OPENAI_API_VERSION=2023-05-15

DEPLOYMENT_NAME=xxxx

Replace the xxxx with your values.

On the terminal, navigate to the top folder of the project, and run the following commands:
1. python -m venv venv
2. source venv/bin/activate
3. pip install --upgrade pip
4. pip install -r requirements.txt
5. cd src
6. python main.py
