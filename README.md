# AI Langchain Documentation Helper

An intelligent Streamlit-based assistant that helps developers navigate and understand the Langchain documentation through an AI-powered chatbot interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)

[Live Demo](https://langchain-docs-chatbot.billycychan.com/)

[Langchain Doc Chatbot Demo.webm](https://github.com/user-attachments/assets/c5825a6b-bcdd-4243-bc9a-84cd1803ea35)


## 🌟 Features

- **AI-Powered Documentation Assistant**: Leverages the Langchain framework to provide contextually relevant responses to documentation queries
- **Interactive Chat Interface**: Clean, user-friendly Streamlit interface for natural conversation flow
- **Source Attribution**: Transparent source tracking for all retrieved information
- **User Profiles**: Customizable sidebar displaying user information and social links
- **Docker Support**: Containerized deployment for consistent development and production environments
- **Performance Monitoring**: Integration with Langsmith for request tracking and analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Docker and Docker Compose (optional)
- Pipenv for dependency management
- Ollama installed locally

### Installation

#### 1. Set Up Ollama
```bash
# Install and pull the required model
ollama pull llama3.2:1b
```

#### 2. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/billycychan/langchain-doc-chatbot
cd langchain-doc-chatbot

# Install dependencies using Pipenv
pipenv install
```

#### 3. Configure Environment
Create `.env` and `.env.docker` files in the project root with the following variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_langchain_project
OLLAMA_BASE_URL=your_ollama_base_url:11434
```

#### 4. Launch Application

Using Docker:
```bash
docker compose up -d
```

Or locally:
```bash
pipenv run streamlit run main.py
```

Access the application at `http://localhost:8501`

## 🛠 Technology Stack

### Core Components
- **Langchain**: Powers the Retrieval-Augmented Generation (RAG) system
- **Langsmith**: Provides request tracing and performance monitoring
- **Pinecone**: Vector database for efficient document embedding storage
- **Streamlit**: Powers the interactive web interface
- **Ollama**: Local model serving for AI capabilities

## 📁 Project Structure

```
langchain-doc-chatbot/
├── backend/
│   └── core.py          # Core Langchain integration logic
├── main.py              # Streamlit application entry point
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Multi-container setup
├── Pipfile             # Python dependencies
└── README.md           # Project documentation
```

## 📬 Contact

Billy Chan - chanc187@mcmaster.ca

Project Link: [https://github.com/billycychan/langchain-doc-chatbot](https://github.com/billycychan/langchain-doc-chatbot)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
