from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pydantic import BaseModel
from .query_understanding_agent import QueryUnderstandingAgent
from .retrieval_agent import RetrievalAgent
from .generation_agent import GenerationAgent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from .context_integration_agent import ContextIntegrationAgent
from schemas.models import RAGResponse
from schemas.models import StringList


def orchestrate_rag(user_query: str, knowledge_base: PDFUrlKnowledgeBase) -> RAGResponse:
    """Orchestrates RAG process with structured validation"""
    try:
        # Phase 1: Query Understanding
        query_agent = QueryUnderstandingAgent()
        query_analysis = query_agent.analyze(user_query)
        # print("Query Understanding Agent: ", query_analysis)

        # Phase 2: Information Retrieval
        retrieval_agent = RetrievalAgent(knowledge_base=knowledge_base)
        retrieval_results = retrieval_agent.retrieve(query_analysis)
        print(type(retrieval_results))
        # print("Retrieval Agent: ", retrieval_results)

        # ✅ Ensure retrieval_results is a list
        if not isinstance(retrieval_results, list):
            retrieval_results = list(retrieval_results)

        # Phase 3: Context Integration
        context_agent = ContextIntegrationAgent()
        augmented_context = context_agent.integrate(query_analysis, retrieval_results)
        # print("Context Integration Agent: ", augmented_context)

        # Phase 4: Response Generation
        generation_agent = GenerationAgent()
        generated_response = generation_agent.generate(augmented_context)
        # print("Generation Agent: ", generated_response)

        return RAGResponse(
            final_answer=generated_response.response
        )

    except Exception as e:
        return RAGResponse(
            final_answer=f"Error processing request: {str(e)}"
        )



