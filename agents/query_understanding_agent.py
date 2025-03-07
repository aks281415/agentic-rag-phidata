from phi.agent import Agent
from phi.model.openai import OpenAIChat
from config.settings import settings
from schemas.models import QueryAnalysis

class QueryUnderstandingAgent:
    def __init__(self):
        self.agent = Agent(
            model=OpenAIChat(model=settings.main_model),
            description="Analyzes and understands user queries",
            instructions=[
                "Break down the user query into four structured components:",
                "- main_topic: The central topic of the query.",
                "- subtopics: A list of related subtopics (can be empty).",
                "- information_type: The type of information being sought (e.g., factual, definition, historical, etc.).",
                "- rephrased_query: A more detailed or clarified version of the query.",
                "Always return all four fields in a structured format."
            ],
            response_model=QueryAnalysis,
            structured_outputs=True
        )

    def analyze(self, query: str) -> QueryAnalysis:
        prompt = f"""
        Analyze the following user query and return a structured response with exactly four fields:

        1️⃣ **main_topic**: The central topic of the query (Always provide a topic).
        2️⃣ **subtopics**: A list of related subtopics (If none exist, return an empty list `[]`, max 3 values).
        3️⃣ **information_type**: The type of information being sought (E.g., factual, opinion, historical, definition, etc.).
        4️⃣ **rephrased_query**: A more detailed or clarified version of the query (If rephrasing is not needed, repeat the original query).

        🔹 **IMPORTANT:** Always return values for all four fields. Do not leave any field empty or as `None`.

        🔍 **User Query:** "{query}"
        """

        response = self.agent.run(prompt)

        return response.content  # This should now always include all four fields

