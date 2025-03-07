# import yaml
# import typer
# import openai
# from agents.orchestrator_agent import orchestrate_rag
# from knowledge_base.vector_store import create_vector_store
# from phi.knowledge.pdf import PDFUrlKnowledgeBase

# def load_config():
#     with open("config/config.yaml", "r") as config_file:
#         return yaml.safe_load(config_file)

# def initialize_knowledge_base(config):
#     vector_db = create_vector_store(
#         collection=config["vector_db"]["collection"],
#         db_url=config["vector_db"]["db_url"]
#     )
#     return PDFUrlKnowledgeBase(
#         urls=config["pdf_urls"],
#         vector_db=vector_db
#     )

# def main():
#     config = load_config()
#     knowledge_base = initialize_knowledge_base(config)
    
#     # # Load the knowledge base: Comment out after first run
#     # knowledge_base.load(recreate=True, upsert=True)
    
#     print("RAG Multi-Agent System Initialized")
#     print("Enter your query (or 'quit' to exit):")
    
#     while True:
#         user_query = input("> ")
#         if user_query.lower() == 'quit':
#             break
        
#         response = orchestrate_rag(user_query, knowledge_base)

#         # # Extract content from the RunResponse object
#         # try:
#         #     if hasattr(response, "content"):  # If response is an object with 'content'
#         #         print("\nResponse:\n")
#         #         print(response.content.strip())  # Extract and print only the actual content
#         #     elif isinstance(response, dict) and "content" in response:  
#         #         print("\nResponse:\n")
#         #         print(response["content"].strip())  # Extract from dictionary
#         #     else:
#         #         print("\nResponse:\n")
#         #         print(str(response).strip())  # Fallback to string conversion if unexpected type

#         # except Exception as e:
#         #     print(f"\nError extracting response: {e}")
#         print(response)

#         print("\n---")

# if __name__ == "__main__":
#     typer.run(main)


import yaml
import typer
from agents.orchestrator_agent import orchestrate_rag
from knowledge_base.vector_store import create_vector_store
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from config.settings import Settings

app = typer.Typer()

def load_config():
    with open("config/config.yaml", "r") as config_file:
        return yaml.safe_load(config_file)

def initialize_knowledge_base(config):
    vector_db = create_vector_store(
        collection=config["vector_db"]["collection"],
        db_url=config["vector_db"]["db_url"]
    )
    return PDFUrlKnowledgeBase(
        urls=config["pdf_urls"],
        vector_db=vector_db
    )

@app.command()
def chat():
    """Start RAG chat interface"""
    settings = Settings()
    config = load_config()
    knowledge_base = initialize_knowledge_base(config)
    
    #run it for the first time to load the knowledge base
    # knowledge_base.load(recreate=True, upsert=True)
    
    print("RAG Multi-Agent System Initialized")
    print("Enter your query (or 'quit' to exit):")
    
    while True:
        user_query = input("> ").strip()
        if user_query.lower() in ('quit', 'exit'):
            break
        
        response = orchestrate_rag(user_query, knowledge_base)
        
        print("\nResponse:")
        print(response)
        print("\n---")

if __name__ == "__main__":
    app()
