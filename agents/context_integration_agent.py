from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pydantic import BaseModel
from typing import List
from config.settings import settings

class IntegratedContext(BaseModel):
    original_query: str
    integrated_information: str
    highlighted_discrepancies: List[str]

class ContextIntegrationAgent:
    def __init__(self):
        self.agent = Agent(
            model=OpenAIChat(model=settings.main_model),
            description="Integrates retrieved information with the original query.",
            instructions=[
                "Combine the original query with relevant retrieved information.",
                "Ensure the integrated context is coherent and relevant.",
                "Prepare the augmented prompt for the generation phase.",
                "Highlight any discrepancies or conflicts in the information."
            ],
            response_model=IntegratedContext,
            structured_outputs=True,
            read_chat_history = True
        )

    def integrate(self, query: str, retrieved_info: str) -> IntegratedContext:
        try:
            response = self.agent.run(
                f"QUERY: {query}\n"
                f"RETRIEVED INFO: {retrieved_info}\n"
                "Integrate the query and information, highlighting any discrepancies."
            )
            return response.content
        except Exception as e:
            print(f"Context integration error: {str(e)}")
            return IntegratedContext(
                original_query=query,
                integrated_information="Error occurred during integration.",
                highlighted_discrepancies=[]
            )
