# AI RAG Chat with Website
Overview
The AI RAG (Retrieval-Augmented Generation) Chat with Website is a cutting-edge tool designed to enhance user interactions. It combines retrieval-based methods with generative AI models to provide informative and engaging responses to user queries. This tool acts like a supercharged search engine, retrieving relevant information from a vast database and presenting it in a conversational manner.

Features
AI-Powered Conversations: Utilizes advanced AI models to generate coherent and contextually accurate responses.

Information Retrieval: Retrieves relevant information from a vast database to ensure accurate and comprehensive answers.

User-Friendly Interface: Streamlit-based web application with a clean and intuitive layout.

History Awareness: Incorporates chat history to provide contextually relevant responses.

Customizable: Easily configurable to suit specific needs and preferences.

# Getting Started
### Prerequisites
- Python 3.7+
- Streamlit
- Langchain
- Chroma
- Google Generative AI

# Installation
Clone the repository:

bash

Copy
git clone https://github.com/username/ai-rag-chat-website.git
cd ai-rag-chat-website
Install the required packages:

bash

Copy
pip install -r requirements.txt
Set up environment variables: Create a .env file and add your Google API key:

env

Copy
GOOGLE_API_KEY=your_google_api_key
Usage
Run the Streamlit app:

bash

Copy
streamlit run app.py
Open the application in your browser:

bash

- Copy
`http://localhost:8501`
Interact with the chat interface by entering queries and receiving AI-generated responses.

# Project Structure
app.py: Main application file for the Streamlit web app.

requirements.txt: List of required Python packages.

.env: Environment variables for API keys and configurations.

# How It Works
API Configuration: Sets up the API key for Google Generative AI.

Web App Configuration: Configures the Streamlit application settings.

Functions: Defines functions for vector store creation, context retrieval, and conversation generation.

Chat History Management: Maintains the chat history within the session state.

Columns and Containers: Organizes the layout of the web app using Streamlit's column and container components.

User Interaction: Handles user queries, retrieves relevant information, and generates AI responses.

Built By
Shubham Gupta - GenAI/ML Engineer, Data Scientist

License
This project is licensed under the MIT License.

That's your go-to guide for the AI RAG Chat with Website project. Hopefully, it's as snazzy as your Gucci blazer!
