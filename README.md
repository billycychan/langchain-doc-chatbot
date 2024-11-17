# AI Langchain Documentation Helper

Welcome to the AI Langchain Documentation Helper! This project is a Streamlit-based web application designed to assist users in navigating and understanding the Langchain documentation using an AI-powered chatbot.


[Watch the Demo Video](./demo.webm)

Live: https://langchain-docs-chatbot.billycychan.com/

## Features

- **AI-Powered Chatbot**: Utilizes the Langchain framework to provide intelligent responses to user queries about the Langchain documentation.
- **User Profile Sidebar**: Displays user information and links to social profiles.
- **Source Tracking**: Provides sources for the information retrieved by the AI.

## Getting Started

### Prerequisites

- Python 3.12
- Pipenv for managing dependencies

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/billycychan/langchain-doc-chatbot
   cd langchain-doc-chatbot
   ```

2. **Set up environment variables**:
   - Create a `.env` and `.env.docker` files in the root directory.
   - Add the following environment variables to both `.env` file:

     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     PINECONE_API_KEY=your_pinecone_api_key
     LANGCHAIN_TRACING_V2=true
     LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
     LANGCHAIN_API_KEY=your_langchain_api_key
     LANGCHAIN_PROJECT=your_langchain_project
     OLLAMA_BASE_URL=your_ollama_base_url:11434
     ```
3 **Run Docker**
   - run `docker compose up -d`
4. **Access the application**:
   - Open your web browser and go to `http://localhost:8501`.

## Usage

- Enter your query in the prompt input field.
- The AI will generate a response based on the Langchain documentation.
- View the response and its sources in the chat interface.

## Technologies and Frameworks

This project leverages several cutting-edge technologies and frameworks to deliver a robust and efficient AI-powered documentation helper:

1. **Langchain**: Utilized to build a Retrieval-Augmented Generation (RAG) application. Langchain provides the necessary tools to integrate language models and retrieval systems, enabling the application to generate accurate and contextually relevant responses.

2. **Langsmith**: Employed to keep track of each request made to the application. Langsmith offers tracing and monitoring capabilities, ensuring that each interaction is logged and can be analyzed for performance and accuracy.

3. **Pinecone**: Used as a vector database to store and retrieve document embeddings. Pinecone's high-performance vector search capabilities allow the application to efficiently find and retrieve relevant documents based on user queries.

4. **Streamlit**: The framework used to build the frontend of the application. Streamlit provides an interactive and user-friendly interface, making it easy for users to input queries and view responses in real-time.

These technologies work together to create a seamless experience for users seeking information from the Langchain documentation.

## Project Structure

- `backend/core.py`: Contains the core logic for interacting with the Langchain framework.
- `main.py`: The main entry point for the Streamlit application.
- `Pipfile`: Lists the project dependencies.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

For any questions or feedback, please contact Billy Chan at {chanc187} at mcmaster.ca]
