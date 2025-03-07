import os
import yaml
from pathlib import Path

class Settings:
    def __init__(self):
        self.config_path = Path("config/config.yaml")
        self._load_config()
        
    def _load_config(self):
        with open(self.config_path) as f:
            self.config = yaml.safe_load(f)
        
        # OpenAI Settings
        self.openai_api_key = os.getenv("OPENAI_API_KEY") or self.config["openai"]["api_key"]
        
        # VectorDB Settings
        self.pgvector_db_url = self.config["vector_db"]["db_url"]
        self.pgvector_collection = self.config["vector_db"]["collection"]
        
        # Agent Settings
        self.main_model = self.config["models"]["main"]
        self.embedding_model = self.config["models"]["embedding"]

settings = Settings()
