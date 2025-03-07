# Multi-Agent RAG System

This project implements a Retrieval Augmented Generation (RAG) system using multiple specialized agents powered by Phidata.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key in `config/config.yaml`
4. Add your PDF URLs to `config/config.yaml`

## Usage

Run the main script:

python main.py


Enter your queries when prompted. Type 'quit' to exit.

## Structure

- `agents/`: Contains individual agent implementations
- `knowledge_base/`: Manages the vector database
- `utils/`: Utility functions for embeddings and text splitting
- `config/`: Configuration files
- `main.py`: Entry point of the application

## Extending

To add new agents or modify existing ones, edit the corresponding files in the `agents/` directory.
