from phi.agent import Agent
from config.settings import settings
from phi.model.openai import OpenAIChat
from schemas.models import RetrievedDocument
from schemas.models import QueryAnalysis
from schemas.models import RetrievedDocumentsResponse 

class RetrievalAgent:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

        self.agent = Agent(
            model=OpenAIChat(model=settings.main_model),
            knowledge_base=self.knowledge_base,
            description="Retrieves relevant information from the knowledge base.",
            instructions=[
                "Use the query to search the knowledge base.",
                "Retrieve the most relevant documents or passages.",
                "Rank and filter the retrieved information based on relevance.",
                "Summarize the retrieved information if it's too lengthy."
            ],
            response_model=RetrievedDocumentsResponse,
            read_chat_history = True,
            structured_outputs=True
        )

    def retrieve(self, query_analysis: QueryAnalysis) -> list[RetrievedDocument]:
        return self.agent.run(
            f"Retrieve information for: {query_analysis.rephrased_query or query_analysis.main_topic}"
        ).content

